#!/usr/bin/python
# Ha, and you thought I'd commit code.

from twitter import *;

# a file with two lines. The first is your email, the second is your password
f = open("_config")
email =  f.readline();
pw = f.readline();

email = email.strip();
pw = pw.strip();

temp = Twitter(email,pw);
i = 0;

for status in temp.statuses.user_timeline(count=50):
	i += 1;
	print str(i) + ": " + status['text'];

