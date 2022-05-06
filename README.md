# netbox-plugin-unique-fields

## Introduction

This plugin adds the functionality of unqiue enforced configurable fields in Netbox. 
Right now, it only supports a specific field for one specific use case but may be extended later on as needed.

## ToDos

+ Publication on PyPi for easier installation

## Installation

+ Install `netbox-plugin-unique-fields`
+ Add `netbox-plugin-unique-fields` to PLUGINS

## Usage

This plugin adds a panel in a Device detail view on the right hand side. It shows the current SID of the device or shows an Add button to indicate the possibility to add an SID to this device.

![Screenshot from 2022-05-06 15-40-36](https://user-images.githubusercontent.com/12380026/167146557-deca5a90-fe28-4d69-8d16-1128c185aad0.png)

It adds a form to assign a SID to a device.

![Screenshot from 2022-05-06 15-40-51](https://user-images.githubusercontent.com/12380026/167146636-eb8a5ddd-3bfb-4647-98dc-ac2de092e680.png)

After a successful creation, it shows the current SID within the Devices detail view.

![Screenshot from 2022-05-06 15-41-07](https://user-images.githubusercontent.com/12380026/167146753-dbd73196-140f-4401-87c9-69df6e912a19.png)

## API

This plugin also features an API. This is viewable under `api/plugins/unique_fields/`. 
`api/plugins/unique_fields/sids` provides a list of all assigned SIDs in the following form:
```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 8,
            "device": {
                "id": 1,
                "url": "http://127.0.0.1:8000/api/dcim/devices/1/",
                "display": "Firma Gerät (1)",
                "name": null,
                "display_name": "Firma Gerät (1)"
            },
            "sid": 525555,
            "created": "2022-05-06",
            "last_updated": "2022-05-06T13:40:58.134122Z"
        }
    ]
}
```


