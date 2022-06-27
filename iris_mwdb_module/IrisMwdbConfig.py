#!/usr/bin/env python3
#
#
#  IRIS MWDB Source Code
#  Copyright (C) 2022 - DFIR-IRIS
#  contact@dfir-iris.org
#  Created by DFIR-IRIS - 2022-06-27
#
#  License Apache Software License 3.0

module_name = "IrisMWDB"
module_description = ""
interface_version = 1.1
module_version = 1.0

pipeline_support = True
pipeline_info = {
    "pipeline_internal_name": "MWDB_pipeline",
    "pipeline_human_name": "MWDB Pipeline",
    "pipeline_args": [
        ['MWDB_arg', 'optional']
    ],
    "pipeline_update_support": True,
    "pipeline_import_support": True
}


module_configuration = [
    {
        "param_name": "mwdb_url",
        "param_human_name": "MWDB URL",
        "param_description": "",
        "default": None,
        "mandatory": True,
        "type": "string"
    },
    {
        "param_name": "mwdb_key",
        "param_human_name": "MWDB key",
        "param_description": "MWDB API key",
        "default": None,
        "mandatory": True,
        "type": "sensitive_string"
    },
    
]