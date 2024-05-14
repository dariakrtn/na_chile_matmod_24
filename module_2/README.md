# Chess Video Improver

### Note
currently don't work

### Main Idea
Given a video of chess match & pgn file of this game create an interesting & dynamic video.

> echo "pizza cost = 969"

---

### Installation

#### Linux

```console
git clone https://github.com/dariakrtn/na_chile_matmod_24.git

cd na_chile_matmod_24/module_2

sudo docker compose up
```
by default will be available at http://127.0.0.1:8501

#### Windows
```
echo nope
``` 


Для работы приложения нужно пополнить аккаунт в ProxyAPI\
При использовании разных моделей Chatgpt, результат сильно рознится.\
Лучше всего использовать модель gpt-4o. 

Цена запроса ~30 рублей.\
Вставить свой token от ProxyAPI, нужно в **api_promt** \
proxyapi.ru 

```api_key="TOKEN_PROXYAPI"``` 

Также нужно сгенерировать token read для HuggingFace\
Вставить свой token от HuggenFace, нужно в creat_audio_comment\
```headers = {"Authorization": f"Bearer TOKEN_HuggingFace"}```


Для получение тестовых токенов написать https://t.melDeeDl 