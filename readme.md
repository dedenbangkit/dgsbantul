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
python live.py <NIK> blank
```

To show datawithout parameters

```
python live.py <NIK> c
```

### Offline

Saving dataset to file for fast search by replacing `live.py` with `app.py`
Note: that we need to have dataset which collected with `cron.py` before running
To save datasets:

```
python cron.py
```
