import requests
import time
import json
from datetime import datetime

class VKBanManager:
    def __init__(self):
        self.tokens_file = "tokens.json"
        self.blacklist_file = "blacklist.txt"
        self.load_config()

    def load_config(self):
        try:
            with open(self.tokens_file, 'r') as f:
                self.tokens = json.load(f)
        except FileNotFoundError:
            self.tokens = []
        
        try:
            with open(self.blacklist_file, 'r') as f:
                self.blacklist = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            self.blacklist = []

    def save_tokens(self):
        with open(self.tokens_file, 'w') as f:
            json.dump(self.tokens, f, indent=4)

    def add_token(self, new_token):
        if new_token not in self.tokens:
            self.tokens.append(new_token)
            self.save_tokens()
            return True
        return False

    def ban_user(self, token, user_id):
        url = "https://api.vk.com/method/account.ban"
        params = {
            "access_token": token,
            "v": "5.131",
            "owner_id": user_id
        }
        response = requests.post(url, params=params)
        return response.json()

    def unban_user(self, token, user_id):
        url = "https://api.vk.com/method/account.unban"
        params = {
            "access_token": token,
            "v": "5.131",
            "owner_id": user_id
        }
        response = requests.post(url, params=params)
        return response.json()

    def process_blacklist(self, action):
        results = []
        for token in self.tokens:
            for user_id in self.blacklist:
                try:
                    if action == "ban":
                        result = self.ban_user(token, user_id)
                    else:
                        result = self.unban_user(token, user_id)
                    
                    results.append({
                        "token": token[:10] + "...",
                        "user_id": user_id,
                        "result": result
                    })
                    
                    time.sleep(0.3)  # Задержка между запросами
                    
                except Exception as e:
                    results.append({
                        "token": token[:10] + "...",
                        "user_id": user_id,
                        "error": str(e)
                    })
        return results

def main():
    manager = VKBanManager()
    
    while True:
        command = input("Введите команду (/ban, /unban, /add_token, /exit): ").strip().lower()
        
        if command == "/exit":
            break
            
        elif command == "/add_token":
            token = input("Введите новый токен: ").strip()
            if manager.add_token(token):
                print("Токен успешно добавлен!")
            else:
                print("Токен уже существует!")
                
        elif command in ["/ban", "/unban"]:
            action = "ban" if command == "/ban" else "unban"
            results = manager.process_blacklist(action)
            
            for result in results:
                if 'error' in result:
                    print(f"Ошибка для {result['user_id']}: {result['error']}")
                else:
                    print(f"Успешно обработан {result['user_id']} с токеном {result['token']}")
                    
        else:
            print("Неизвестная команда")

if __name__ == "__main__":
    main()