# config/views.py
from django.views.generic import TemplateView
import requests
import json
import praw
from django.http import HttpResponse
from django.shortcuts import render
import environ

import os
from config import *



class Home(TemplateView):
    template_name = 'home.html'
    reddit = praw.Reddit(
        client_id='69d3ai0Y9ek4Vg',
        client_secret='y5zpeDJm_J8JwIMn4hQFHwH7_gs',
        redirect_uri="http://localhost:8000",
        user_agent="django:reddittoplinks:1.0 (by /u/haharshita)",
     )


    page = reddit.subreddit('aww')
    top_posts = page.hot(limit=10)
    for post in top_posts:
        print(post.title, post.ups)

