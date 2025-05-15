from swift.llm import InferRequest, InferClient, RequestConfig
from swift.plugin import InferStats


MAX_TOKENS = 4096
engine = InferClient(host='127.0.0.1', port=8000)
print(f'models: {engine.models}')
metric = InferStats()
request_config = RequestConfig(max_tokens=MAX_TOKENS, temperature=0)

# 这里使用了3个infer_request来展示batch推理
# 支持传入本地路径、base64和url


# base64
import base64
import requests
resp = requests.get('https://modelscope-open.oss-cn-hangzhou.aliyuncs.com/images/baby.mp4')
base64_encoded = base64.b64encode(resp.content).decode('utf-8')
messages = [{'role': 'user', 'content': [
    {'type': 'video', 'video': f'data:video/mp4;base64,{base64_encoded}'},
    {'type': 'text', 'text': 'describe the video'}
]}]
infer_request = InferRequest(messages=messages)
request_config = RequestConfig(max_tokens=512, temperature=0, stream=True)
gen_list = engine.infer([infer_request], request_config, metrics=[metric])
print(f'response0: ', end='')
for chunk in gen_list[0]:
    if chunk is None:
        continue
    print(chunk.choices[0].delta.content, end='', flush=True)
print()
print(metric.compute())