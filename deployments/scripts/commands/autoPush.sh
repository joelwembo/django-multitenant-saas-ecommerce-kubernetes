git config --global user.name "wjengine.devops"
git config --global user.email "wjengine.devops"
git config --global user.password "glpat-37tdx8wcWYy-PH4W4jxj"
git config credential.helper store

git status
git add .
echo 'Enter the commit message:'
# shellcheck disable=SC2162
read commitMessage

git commit -m "$commitMessage"

#echo 'Enter the name of the branch:'
#read branch

#git push origin $branch
git push origin main

read