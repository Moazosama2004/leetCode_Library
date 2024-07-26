class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        items_validate = 0

        if ruleKey == 'type' :
            for item in items :
                if item[0] == ruleValue :
                    items_validate += 1
        elif ruleKey == 'color' :
            for item in items :
                if item[1] == ruleValue :
                    items_validate += 1
        elif ruleKey == 'name' :
            for item in items :
                if item[2] == ruleValue :
                    items_validate += 1
        return items_validate

