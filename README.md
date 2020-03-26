[![Build Status](https://travis-ci.org/sammyfung/COVID-19-HK-DH.svg?branch=master)](https://travis-ci.org/sammyfung/COVID-19-HK-DH)

# Hong Kong Department of Health - Wuhan Virus Data Scraper

It is a simple scraper to return daily confirmed/deaths/recovered numbers of COVID-19 'Wuhan' Coronavirus Cases in Hong Kong from the [data source](https://data.gov.hk/en-data/dataset/hk-dh-chpsebcddr-novel-infectious-agent/resource/05e8a593-1469-4348-937d-2746afd11442) provided by Department of Health in Hong Kong.

Data are outputted to standard output in CSV syntax of [JHU CSSE's COVID-19 project](https://github.com/CSSEGISandData/COVID-19).

## Usages

To list the latest accumlated confirmed/deaths/recovered cases in Hong Kong:

```
python3 hk_dh_wuhan_data.py 
```

To list the accumlated confirmed/deaths/recovered cases on the specific date in Hong Kong:

```
python3 hk_dh_wuhan_data.py 20200301
```

To list the accumlated confirmed/deaths/recovered cases on each days in Hong Kong:

```
python3 hk_dh_wuhan_data.py ALL
```

## Permissive Open Source License

Copyright 2020 Sammy Fung

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
