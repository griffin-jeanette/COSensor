# Raspberry Pi Carbon Monoxide Sensor

## Getting Started
These instructions will allow you to recreate this project on your local machine and raspberry pi
in order to run the sensor.

### Built With
  * [Flask](https://flask.palletsprojects.com/en/1.1.x/) - for web development
  * [Twilio](https://www.twilio.com/) - automated text messages
  * [Gmail API](https://developers.google.com/gmail/api) - automated emails

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
In order to configure the gmail API, first of all you need to visit the [google dashboard](https://console.developers.google.com/projectselector2/apis/dashboard?supportedpurview=project). Here you can register the new project using the ‘create project’ option. After the new project is created, there will be a prompt which says “You don’t have any APIs available to use yet. To get started, please visit API Library”. 
Then visit [here](https://console.developers.google.com/apis/librar...). In the search box there select the Gmail API. After you click the Gmail API option, there will be an option to Enable this API. After you enable the Gmail API, you will need to create credentials for you to be able to use it. Therefore click on “Create Credentials”, this will take you to the window asking you to select the API. There, select the Gmail API, then select the right option of where you will be calling this Gmail API from. After this you will need to select your role: something like product owner. Then the json file will be downloaded to your computer, which will be your service account, copy and paste this inside cred folder in your project directory. Hurray then your API is enabled and your account is registered to use this Gmail API. Now comes the fun part, say we want to send an email using your account registered with Gmail API. Visit [this website](https://console.developers.google.com/apis/librar...) for reference about code and how the code works to send email from the registered account. The first thing to remember is to define the SCOPE that allows you to send email. The scope to send email looks like: “https://www.googleapis.com/auth/gmail.send”. You can find the list of authorization scopes [here.](https://console.developers.google.com/apis/librar...)
Everything you do using the Gmail API like access the labels of email, or send the email, the new pickle token is created, this happens for the first time you run the application. Every time after that if you add a new scope the new token pickle is created, which allows for all the functions you can carry out using the gmail API. Each time you run your application changing the scope the new pickle token is created.

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


### Authors
  * Griffin Jeanette
  * Pritam Basnet
