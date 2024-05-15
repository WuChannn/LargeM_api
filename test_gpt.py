from gpts.run_gpt import run
from gpts.access_token import get_access_token

from utils.read_file import read_file


if __name__ == "__main__":

    # app_id 和 app_key 是研究院分配给你的
    app_id = "YOUR_APP_ID"
    app_key = "YOUR_APP_KEY"
    access_token = get_access_token(app_id, app_key)

    instruction_str = read_file('./assets/prompt')
    instruction_response = run(instruction_str, app_id, app_key, access_token)
    instruction_response_str = instruction_response['data']['content']

    input_str = f"User: {instruction_str}\nAI: {instruction_response_str}\n"

    input_str += "请帮我完成一份关于布局生成模型在PPT页面美化中的专利交底书，需要涉及布局生成模型的具体细节\n"

    print('Input:', input_str)

    response = run(input_str, app_id, app_key, access_token)
    response_str = response['data']['content']

    print('Reply:', response_str)

    print('-' * 50)