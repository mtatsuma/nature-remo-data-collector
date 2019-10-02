# Nature Remo Sensor Data Collector

Collect sensor data via Nature Remo cloud API and store the data on
Google spread sheet.

## Description

[Nature Remo](https://nature.global/) smart remote controller has some
kinds of sensor, which can measure the temperature, humidity,
illumination and human motions.

This collector written by Python3 calls Nature Remo cloud API and
Google Spread Sheet API to collect and store the sensor data.

This collector can be run on [Heroku](https://www.heroku.com/home)
service, which provides a platform to run your own Python apps.

![Architecture](https://user-images.githubusercontent.com/48573325/66041590-29eeaf80-e555-11e9-9b0f-556cc083c392.jpg)

![sensor_data_nature_remo_1](https://user-images.githubusercontent.com/48573325/66041666-573b5d80-e555-11e9-9ea6-efd2689c268e.png)

## Requirement

- [Nature Remo Smart Controller](https://nature.global/)

### To run local environment

- Python 3.7.4
- Packages listed in requirements.txt

### To run on Heroku

- [Heroku](https://www.heroku.com/home) account setup

## Usage

### Setup Google API credential

1. Enable Google Drive API and service acount from [Google Developers
Console](https://console.developers.google.com/project).

2. Create a spread sheet and share it with the service account.

### Configuration

You must configure the following environmental variables.

| Env. variables | Required | Description |
|:---------------|:---------|:------------|
| REMO_TOKEN | yes | Token for Nature Remo Cloud API |
| SHEET_NAME | yes | Name of Google SpreadSheet to store sensor data |
| GS_CREDENTIAL_TYPE | yes | From Google API service account key |
| GS_PROJECT_ID | yes | From Google API service account key |
| GS_PRIVATE_KEY_ID | yes | From Google API service account key |
| GS_PRIVATE_KEY | yes | From Google API service account key |
| GS_CLIENT_EMAIL | yes | From Google API service account key |
| GS_CLIENT_ID | yes | From Google API service account key |
| GS_AUTH_URI | yes | From Google API service account key |
| GS_TOKEN_URI | yes | From Google API service account key |
| GS_AUTH_PROVIDER_CERT_URL | yes | From Google API service account key |
| GS_CLIENT_CERT_URL | yes | From Google API service account key |
| REMO_CLOCK_INTERVAL | no | Interval (min) to collect the sensor data on Heroku custom clock scheduler |

To set these variables, you can edit `samples/remorc.sh` and source it.

### Run on local environment

Clone source code.
```
$ git clone https://github.com/mtatsuma/nature-remo-data-collect.git
$ cd nature-remo-data-collect
```

Edit `samples/remorc.sh` and set environment variables.
```
$ source remorc.sh
```

Run the worker.py
```
$ python worker.py
```

### Run on Heroku

Clone source code.
```
$ git clone https://github.com/mtatsuma/nature-remo-data-collect.git
$ cd nature-remo-data-collect
```

Login Heroku. Heroku CLI must be installed.
```
$ heroku login
```

Create heroku app.
```
$ heroku create <app-name>
```

Push heroku app.
```
$ git push heroku master
```

Edit `samples/remoheroku.sh` and configure heroku app
```
$ source remoheroku.sh
```

Run the apps periodically (default 1min interval).
```
$ heroku ps:scale clock=1
```

## Author

[mtatsuma](https://github.com/mtatsuma)
