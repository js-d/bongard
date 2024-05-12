import os
import anthropic
import base64



def load_prompt():
    with open("prompt.txt", "r") as file:
        return file.read()

main_prompt = load_prompt()



def image_group_content(problem, side):
    group_content = []
    group_content.append({"type": "text", "text": f"The following 6 images form the '{side}' group."})
    for i in range(1, 7):
        with open(f"problems/{problem}/{side}_image_{i}.png", 'rb') as image_file:
            image_base64 = base64.b64encode(image_file.read()).decode("utf-8")
            group_content.append(
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/png",
                        "data": image_base64,
                    },
                }
            )
    return group_content


def problem_content(problem):
    content = [{"type": "text", "text": "What follows is a Bongard problem."}]
    content.extend(image_group_content(problem, "left"))
    content.extend(image_group_content(problem, "right"))
    content.append({"type": "text", "text": main_prompt})
    return content

def get_response(problem, model):
    client = anthropic.Anthropic()
    content = problem_content(problem)
    message = client.messages.create(
        model=model,
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": content
            }
        ],
    )
    return message


if __name__ == "__main__":
    model = "claude-3-opus-20240229"
    # model = "claude-3-haiku-20240307"
    for problem in range(49, 101):
        print(f"Processing problem number: {problem}")
        message = get_response(problem, model)
        response_content = message.content[0].text
        problem_folder = f"problems/{problem}/{model}"
        os.makedirs(problem_folder, exist_ok=True)
        with open(f"{problem_folder}/response.txt", 'w') as file:
            file.write(response_content)

