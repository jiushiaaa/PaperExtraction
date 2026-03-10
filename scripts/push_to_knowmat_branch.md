# 将本项目推送到 PaperExtraction knowmat 分支

因公司环境只能通过 git 传递，需将 **data/raw** 与 **data/processed** 一并提交。

## 一、已做修改

- 已删除 `data/processed/.gitignore`，使 `data/processed` 下所有抽取结果可被 git 跟踪并提交。

## 二、在项目根目录执行（PowerShell 或 CMD）

### 若当前目录还不是 git 仓库

```powershell
cd D:\knowmat2

git init
git remote add origin https://github.com/jiushiaaa/PaperExtraction.git
git fetch origin knowmat
git checkout -b knowmat
git branch -u origin/knowmat

git add .
git status
git commit -m "knowmat: sync local changes and include data/raw, data/processed"

git push -u origin knowmat
```

### 若已是 git 仓库且已有 origin

```powershell
cd D:\knowmat2

git fetch origin knowmat
git checkout knowmat
# 若本地没有 knowmat 分支： git checkout -b knowmat origin/knowmat

git add .
git add data/raw data/processed
git status
git commit -m "knowmat: include data/raw and data/processed for transfer"

git push origin knowmat
```

### 若远程已有 knowmat 分支且要覆盖

```powershell
git checkout knowmat
git add .
git commit -m "knowmat: sync with data/raw and data/processed"
git push origin knowmat --force
```

## 三、注意

- 推送前确认 **.env** 未被加入（根目录 .gitignore 已忽略 .env，勿强制 add）。
- 若仓库体积过大，可考虑用 Git LFS 管理 data 下大文件（可选）。
