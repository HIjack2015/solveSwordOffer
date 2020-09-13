

def check():
    target = input().strip()
    target_len=len(target)
    for i in range(target_len):
        this_len=target_len-i
        for start in range(0,i+1):
            if is_ok(target[start:this_len+start]):
                print(str(this_len))
                return
    return False
def is_ok(to_check:str):
    print("check  "+to_check)
    if not to_check:
        return False
    eles=['a','b','c','x','y','z']
    for ele in eles:
        if to_check.count(ele)%2!=0:
            return False
    return True

check()