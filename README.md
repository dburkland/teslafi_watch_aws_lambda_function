README
=========

### Introduction

TeslaFi Watch is an AWS Lambda Function that retrieves the latest vehicle data from [TeslaFi](https://www.teslafi.com/index.php), parses out the relevant State of Charge & Battery Charge Limit values, and formats the output so it can be displayed on an Apple Watch using the Simple Complications watchOS app & complication.

### Setup

To leverage TeslaFi Watch, please follow the steps below:

* Open Safari on your iPhone and browse to [TeslaFi](https://www.teslafi.com/index.php)
* Login to TeslaFi with your existing account credentials
* Now that you are logged into TeslaFi, select "Settings" -> "Account" -> "Advanced" -> "TeslaFi API Access"
* Tap on "Generate" to create a TeslaFi API key
* Please select & copy the generated TeslaFi API key which starts right after "New key is "
* Download the [Simple Complications](https://apps.apple.com/us/app/simple-complications/id1189376822) App to both your Apple Watch & iPhone
  * NOTE: While Simple Complications is free to download, you will need to sign up for the annual subscription in order to actually use the app. The subscription costs $1.99 USD and renews annually.
* Open the Simple Complications (aka "Simple C") App on your iPhone
  * NOTE: If the iPhone app at any time instructs you to open the Simple Complications app on your Apple Watch please do so
* Copy/paste the following URL into the text box underneath "Web URL containing the feed:" making sure to replace TOKEN_GOES_HERE with the TeslaFi API key you generated in the previous steps
  * f92lhpnvwd.execute-api.us-west-1.amazonaws.com/prod?TOKEN=TOKEN_GOES_HERE
  * NOTE: Make sure there are no spaces between the equal sign and the TeslaFi API key
* Next you will want to tap on "JSON" and "Frequent" to select those settings
* Tap on "Setup Data Source" and make sure "Data" is selected
* In the text box below "'Path' to your object'" please enter "body" without the double quotes
* Tap on "Design" and make sure "Text" is selected, "Low number (for gauge)" & "High number (for gauge)" are set to 0, and that "Decimal places" is set to "10"
* Tap on "Back" in the upper left corner to return to the main screen
* We will then save the TeslaFi preset by tapping on the slider button underneath "Setup Data Source" and then by selecting "Save Current"
* In the "New Preset" window enter "TeslaFi" (again without double quotes) and tap "Done"
* Tap on "Back" in the upper left corner to return to the main screen
* Tap on "Update Watch" to push the changes to your Apple Watch
* To add the Simple C watch complication to your watch face, please open the "Watch" app on your iPhone
* With the "Watch" app now open, tap on the desired watch face under "MY FACES"
* Once you have decided where the complication will reside on your watch face, tap the existing value in the appropriate line and select "Simple C" from the list
* Tap on your watch's name in the upper left to exit and save the changes
* At this point the watch complication should be displaying data from TeslaFi Watch like in the following screenshot:
  * ![](https://pbs.twimg.com/media/Ebs_THNWAAIok1Y?format=jpg&name=small)

### FAQs

* At a high level, how does the TeslaFi Watch API service work?
  * Simple C watchOS App & Complication -> AWS API Gateway -> AWS Lambda Function -> TeslaFi API Service
* Will TeslaFi Watch keep my Tesla awake?
  * No, TeslaFi Watch will NOT keep your Tesla awake since it is merely displaying data that was already collected by TeslaFi.
* How do I force the Simple C complication to retrieve the latest data from TeslaFi?
  * Tap on the Simple C complication on your Apple Watch and then tap "Force Update". This process usually takes a few seconds to complete however if you run into any issues or receive any error messages feel free to reach out.
* How secure is TeslaFi Watch?
  * When the watch complication attempts to retrieve the latest data, the TeslaFi API key is sent to the TeslaFi Watch API service using TLS where it is then used to communicate with TeslaFi. The authentication token is never logged or recorded in any way, shape or form.
  * NOTE: I do NOT log or record any usage data, nor do I log or record any of the generated Tesla or TeslaFi API tokens.
