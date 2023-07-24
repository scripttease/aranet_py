# Connecting to Aranet4 CO2 monitor with Python.

## Quickstart

```sh
# run discover.py to get UUID of your Aranet4 device
python discover.py
```

Create a `.env` file with your Aranet4 UUID from previous step, see `example.env`

Collect readings from your device IF you have allowed remote connection via the Aranet4 app.

```sh
python main.py
```
