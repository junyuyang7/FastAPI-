from typing import Union
from fastapi import FastAPI, Query

app = FastAPI()

@app.get('/items/')
async def read_items(q: Union[str, None] = Query(
    default='None', max_length=50, min_length=3, regex='^aaa',
     title='Query String', alias='item-query', deprecated=False)):
    result = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}]}
    if q:
        result.update({'q': q})
    return result

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)

# 总结
# 你可以为查询参数声明额外的校验和元数据。

# 通用的校验和元数据：

# alias
# title
# description
# deprecated
# 特定于字符串的校验：

# min_length
# max_length
# regex
# 在这些示例中，你了解了如何声明对 str 值的校验。