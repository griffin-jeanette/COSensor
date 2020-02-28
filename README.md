# Raspberry Pi Carbon Monoxide Sensor

### Installing Packages
Since you may not already have all the necessary packages installed, we need to install them using pip:
```
pip install flask flask_restful flask_wtf requests
```

### Setting Up Twilio
Since our program alerts us through text messages when the Carbon Monoxide levels become too high, we need to be able to send messages from a central number. To do this, we will use a platform called Twilio. First, [sign up](https://www.twilio.com/try-twilio) for a free trial account. Next, we need to download a few packages. If you already have Node.js installed with version v8.0.0 or above, skip to step 2. You can check your version with:
```
node -v
```
The first package is Node.js which can be downloaded from their site [here](https://nodejs.org/en/download/). Make sure to installer for your correct operating system, and then open it and follow the prompted instructions.

Next, we need to install the Twilio CLI. This is installed and updated with the Node package manager with the following commands:
```
npm install twilio-cli -g
npm install twilio-cli@latest -g
```
At this point, we need to connect the Twilio CLI to our account. To do this, we need two pieces of information: our Account SID and Auth Token from the [Twilio Console](https://www.twilio.com/login?g=/console?&t=2b1c98334b25c1a785ef15b6556396290e3c704a9b57fc40687cbccd79c46a8c). 
Then run twilio login and enter the information prompted.
```
twilio login
```
So now we have connected our account but still need a phone number. You can purchase one through Twilio with the trial money you have been given. After typing the command below, a bunch of number will pop up; pick one.
```
twilio phone-numbers:buy:local --country-code US --sms-enabled
```
Now, in order for Twilio to work in our program, we need to install its packages. Type
```
pip install twilio
```
Inside the keys.py file, we need to enter in our Account SID and Auth Token for later use. There should already be a blank spot for you to copy and paste these values.
```
passwords = {"twilio":{"account_sid": "paste your sid here",
	     "auth_token": "paste your token here"}}
```
With all this done, it is now time to set up email compatability with our program through the Gmail API.

### Setting Up Gmail


### Running Your Code
Before running the program, change the ip address in the sensor.py file to be the ip address of your computer.
Then, scp it to the pi
```
scp sensor.py pi@"enter pi ip address here":.
```

On the raspberry pi, run the following command:
```
python3 sensor.py
```
On your computer run:
```
python api.py
```
