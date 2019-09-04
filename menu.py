#require _ = require('lodash')
import random
 
# const foods = ['피자','타코','탕수육','치킨']
foods = ['피자','타코','탕수육','치킨']

# console.log(_.sample(foods))
print(random.choice(foods))

# 오브젝트는 중가로 사용
good = {
    '백운동 막국수' : '이베리코 돼지고기',
     '고겟마루': '닭도리탕',
      '대우식당': '부대찌개'
}

#good.고겟마루 사용 XXX
print(good['고겟마루'])

