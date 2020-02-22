# SISKES JOGJA FINDER

## Requrements

Python 3.6 >

## Installation

```
pip install -r requrements.tx
```

## Environment Setup 

```
export identity="LOGIN_USERNAME"
export username="LOGIN_PASSSWORD"
```

## Usage


### Online

To show data with parameters

```
python app.py <NIK> blank online
```

To show data without parameters

```
python app.py <NIK> clean online
```

### Offline

To show data with parameters

```
python app.py <NIK> blank
```

To show data without parameters

```
python app.py <NIK> clean
```

Note: that we need to have dataset which collected with `cron.py` before running
To save datasets:

```
python cron.py
```
