#coding=utf-8

# Name:         test_yaml
# Description:  
# Author:       hao.fan
# Date:         2020/8/23
import yaml


def test_yaml2():
    env = {
        "default": "test",
        "test-env": {
            "dev": "127.0.0.1",
            "test": "yjy.zhiyousx.com:8765"
        }
    }

    with open("env.yaml","w") as f:
        yaml.safe_dump(data=env,stream=f)