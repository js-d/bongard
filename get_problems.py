import requests
import os
import multiprocessing

def download_image(url, folder, filename):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        os.makedirs(folder, exist_ok=True)
        with open(os.path.join(folder, filename), 'wb') as file:
            file.write(response.content)

def scrape_bongard_problem(problem_number):
    url = f"https://oebp.org/BP{problem_number}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        html_content = response.text

        # Calculate the image numbers for left and right images
        left_image_start = (problem_number - 2) * 12 + 8
        right_image_start = left_image_start + 6

        # Download left images
        for i in range(6):
            image_number = left_image_start + i
            image_url = f"https://oebp.org/examples/{image_number}.png"
            download_image(image_url, f"problems/{problem_number}", f"left_image_{i+1}.png")

        # Download right images
        for i in range(6):
            image_number = right_image_start + i
            image_url = f"https://oebp.org/examples/{image_number}.png"
            download_image(image_url, f"problems/{problem_number}", f"right_image_{i+1}.png")

        # Extract the text solution
        search_string = f'<tbody><tr><td valign="top" align="left" width="100"><a href="/BP{problem_number}">BP{problem_number}</a></td><td width="5">'
        start_index = html_content.find(search_string)

        if start_index != -1:
            start_index = html_content.find('</td><td valign="top" align="left">', start_index)
            end_index = html_content.find('</td><td width="2">', start_index)
            if start_index != -1 and end_index != -1:
                solution_text = html_content[start_index + 35:end_index].strip()
                with open(f"problems/{problem_number}/solution.txt", 'w') as file:
                    file.write(solution_text)
            else:
                print(f"Solution not found for Bongard problem {problem_number}")
        else:
            print(f"Solution not found for Bongard problem {problem_number}")

    else:
        print(f"Failed to retrieve Bongard problem {problem_number}")


def worker(problem_number):
    print(f"Processing problem number: {problem_number}")
    scrape_bongard_problem(problem_number)

if __name__ == "__main__":
    problem_numbers = range(70, 80)
    pool = multiprocessing.Pool(processes=4)  # Adjust the number of processes as per the system capability
    pool.map(worker, problem_numbers)
    pool.close()
    pool.join()