print('Auther')
import argparse
import asyncio
import json
import os
import time
import urllib.request
from datetime import datetime, timezone

import aiohttp
import requests
from colorama import Fore, Style, init

#from msauth import login
name = input("Email: ")  
passw = input('Password: ')

def inp(text):
    print(f"{Fore.YELLOW}{text}", end="")
    ret = input("")
    return ret
async def get_mojang_token(email: name, password: passw):
    # Login code is partially from mcsniperpy thx!
    questions = []

    async with aiohttp.ClientSession() as session:
        authenticate_json = {"username": email, "password": password}
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0",
                   "Content-Type": "application/json"}
        async with session.post("https://authserver.mojang.com/authenticate", json=authenticate_json,
                                headers=headers) as r:
            # print(r.status)
            if r.status == 200:
                resp_json = await r.json()
                # print(resp_json)
                auth = {"Authorization": "Bearer: " + resp_json["accessToken"]}
                access_token = resp_json["accessToken"]
                # print(f"{Fore.LIGHTGREEN_EX}Auth: {auth}\n\nAccess Token: {access_token}")
            else:
                print(f"{Fore.LIGHTRED_EX}INVALID CREDENTIALS{Fore.RESET}")

        async with session.get("https://api.mojang.com/user/security/challenges", headers=auth) as r:
            answers = []
            if r.status < 300:
                resp_json = await r.json()
                if resp_json == []:
                    async with session.get("https://api.minecraftservices.com/minecraft/profile/namechange",
                                           headers={"Authorization": "Bearer " + access_token}) as nameChangeResponse:
                        ncjson = await nameChangeResponse.json()
                        print(ncjson)
                        try:
                            if ncjson["nameChangeAllowed"] is False:
                                print(
                                    "Your Account is not"
                                    " eligible for a name change!"
                                )
                                exit()
                            else:
                                print(f"{Fore.LIGHTGREEN_EX}Logged into your account successfully!{Fore.RESET}")
                                print("Your bearer token is: " + access_token)
                        except Exception:
                            print("logged in correctly")
                            print("Your bearer token is: " + access_token)
                else:
                    try:
                        for x in range(3):
                            ans = inp({resp_json[x]["question"]["question"]})
                            answers.append({"id": resp_json[x]["answer"]["id"], "answer": ans})
                    except IndexError:
                        print(f"{Fore.LIGHTRED_EX}Please provide answers to the security questions{Fore.RESET}")
                        return
                    async with session.post("https://api.mojang.com/user/security/location", json=answers,
                                            headers=auth) as r:
                        try:
                            if r.status < 300:
                                print(f"{Fore.LIGHTGREEN_EX}Logged in{Fore.RESET}")
                                print("Your bearer token is: " + access_token)
                        except RuntimeError:
                            print("")
                        if r.status > 300:
                            print(
                                f"{Fore.LIGHTRED_EX}Security Questions answers were incorrect, restart the program!{Fore.RESET}")


asyncio.run(get_mojang_token(name, passw))
os.system('python utils/check.py')