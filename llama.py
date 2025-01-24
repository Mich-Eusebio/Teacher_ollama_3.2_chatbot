import ollama

history = []
            
desiredModel="llama3.2"

def ask_to_llama(prompt):
    global history
    history.append({"role": "user", "content": prompt})
    response = ollama.chat(model=desiredModel, messages=history)
    response = response["message"]["content"]
    history.append({'role': 'assistant', 'content': response})
    return response

if __name__ == "__main__":
    print(ask_to_llama("que es la vida?"))