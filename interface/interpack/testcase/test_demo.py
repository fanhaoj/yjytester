from string import Template

import yaml


class TestDemo:
    def test_retemplate(self):
        data={
            "gytoken":"dsfsdfsdfsfsssfdffffff"
        }
        with open("../data/product.yaml",'r',encoding='utf-8') as f:
            steps=yaml.safe_load(f)
            print(steps)
            re=Template(str(steps)).safe_substitute(data)
            return re