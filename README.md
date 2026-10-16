# Lab 7 - YummyApp CI/CD - 2312777

Bai thuc hanh Mocking GPS, kiem thu ma khuyen mai va GitHub Actions.

## Chay

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
coverage run --source=yummy_app,gps_service -m unittest discover -s . -p "test_*.py"
coverage report -m
coverage html -d coverage_html
coverage report --fail-under=80
```

**Minh chung bat buoc**: can tu chay de tao logs/local_test.log, logs/git_history.log, logs/github_actions_run.log; scan 4 trang viet tay va lap bao cao PDF co link repo + anh Actions. Khong su dung file log gia.

## Anh bai lam viet tay

1. [So do CI Pipeline](docs/handwritten/01-ci-pipeline.jpg)
2. [Tra loi cau hoi CI](docs/handwritten/02-ci-questions.jpg)
3. [Tra loi cau hoi ve thu vien va Pull Request](docs/handwritten/03-dependencies-questions.jpg)
4. [Bang 7 test case Mocking](docs/handwritten/04-mocking-test-cases.jpg)
