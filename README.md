# algorithms

## Environment setup

### 1. Prerequisites

* Python v3.6
* Pip 9.0.1 
* Django v3.0.1
* Virtualenv v16.7.9

### 2. Clone project


```sh
$   git clone https://github.com/Ayasser/algorithms.git
```
    
### 3. Create Virtualenv

```sh
$   virtualenv env
 ```

### 4. Activate Virtualenv

```sh
$ source env/bin/activate
```

### 5. Install required packages inside virtualenv

```sh
$(env)  pip install -r requirements.txt
```

### 6. Verify

```sh
$(env)  python3 manage.py runserver
```
### 7. tests

```sh
$(env)  python3 manage.py test
```
