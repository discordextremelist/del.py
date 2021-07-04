---
description: Documentation in case you don't like the listed examples
---

# Classes, Functions, Errors

{% hint style="info" %}
For responses, please check the API documentation [here](https://discordextremelist.xyz/en-US/docs#api-routes), the responses are the same, except it adds the "time\_taken" key
{% endhint %}

## delpy.Client\(\*args\)

Client class for the wrapper

| Args | Type | Required |
| :--- | :--- | :--- |
| bot | discord.Client | Only when posting |
| token | str | Only when posting |
| loop | ClientSession, EventLoop | No |

## delpy.Client\(\).start\_loop\(\*args\) -&gt; None

Function to start the automatic loop

| Args | Type | Default Value | Minimum Value | Required |
| :--- | :--- | :--- | :--- | :--- |
| wait\_for | int | 1800 | 30 | No |

## delpy.Client\(\).close\_loop\(\) -&gt; None

Function to close the running loop

## delpy.Client\(\).post\_stats\(\*args\) -&gt; \[delpy.errors.HTTPException, dict\]

Function to post the statistics to the API

| Args | Type | Required |
| :--- | :--- | :--- |
| guildCount | int | Yes |
| shardCount | int | No |

## delpy.Client\(\).get\_website\_stats\(\) -&gt; \[delpy.errors.HTTPException, dict\]

Function to get website's statistics

## delpy.Client\(\).get\_website\_health\(\) -&gt; \[delpy.errors.HTTPException, dict\]

Function to get website's health

## delpy.Client\(\).get\_bot\_info\(\*args\) -&gt; \[delpy.errors.HTTPException, dict\]

Function to get information about the bot

| Args | Type | Required |
| :--- | :--- | :--- |
| botid | int | Yes |

## delpy.Client\(\).get\_server\_info\(\*args\) -&gt; \[delpy.errors.HTTPException, dict\]

Function to get information about the bot

| Args | Type | Required |
| :--- | :--- | :--- |
| serverid | int | Yes |

## delpy.Client.get\_template\_info\(\*args\) -&gt; \[delpy.errors.HTTPException, dict\]

Function to get information about the bot

| Args | Type | Required |
| :--- | :--- | :--- |
| templateid | str | Yes |

## delpy.errors.DELpy

Base exception class for the wrapper

## delpy.errors.HTTPException

Raised whenever the API returns status that isn't 200 OK

## delpy.errors.Unauthorized

Raised when you do not provide the token while trying to update the statistics

## delpy.errors.InvalidTime

Raised when the specified time for automatic loop is too short

