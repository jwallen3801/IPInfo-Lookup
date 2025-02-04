# IPInfo-Lookup
This Python script is designed to perform quick lookups of information relating to an IP address or a list of IP addresses on the command line. It queries [ipinfo.io](https://ipinfo.io/) to provide the city, region, country, coordinates, ISP, and postal code associated with a given IP address.

## Usage:
By default, the script takes a single IP address as an argument to perform the lookup.
```
$ python ipinfo_lookup.py <IP Address>
```

You can also provide a file containing a newline-separated list of IP addresses for a batch lookup of all of them.

```
$ python ipinfo_lookup.py -f <file>
```

Example:
```
$ python ipinfo_lookup.py 8.8.8.8
IP info for 8.8.8.8:
===============================
City: Mountain View
Region: California
Country: US
Location: 37.4056,-122.0775
ISP: AS15169 Google LLC
Postal Code: 94043
===============================
```

## Compatability:
This script is compatible with Python 3.x.

## Acknowledgements:
Special thanks to [ipinfo.io](https://ipinfo.io/) for providing the data for this script.
