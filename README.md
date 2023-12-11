# axlfc.github.io

This repository contains the source code for my personal portfolio webpage hosted on GitHub Pages.

[![Visit My Code Portfolio](https://img.shields.io/badge/Visit-Code%20Portfolio-blue?style=for-the-badge&logo=github)](https://axlfc.github.io)


## Overview

The webpage is built using Bootstrap 4 for GitHub Pages and serves as a showcase for my projects, skills, and accomplishments.

## GitHub Pages Overview

[GitHub Pages](https://pages.github.com/) is a static site hosting service provided by GitHub, allowing users to create and publish webpages directly from their GitHub repositories. GitHub Pages supports Jekyll, a static site generator, and provides flexibility with HTML, CSS, and JavaScript for building your site.

## Creating Your Own GitHub Pages

1. **Create a Repository:**
   - Go to your GitHub profile.
   - Click on the "Repositories" tab.
   - Create a new repository with the name `username.github.io`, replacing "username" with your GitHub username.

2. **Clone the Repository:**
   - Open your terminal or Git Bash.
   - Run the following command, replacing "username" with your GitHub username:
     ```bash
     git clone https://github.com/username/username.github.io.git
     ```

   **Explanation:**
   - Use `git clone` to clone a repository from a URL.
   - The URL is the address of your GitHub repository, creating a copy on your local machine.

3. **Add Your Content:**
   - Customize your webpage by adding HTML, CSS, and other assets.

   **Explanation:**
   - Create or modify files in the cloned repository based on your webpage's content.

4. **Commit Your Changes:**
   - Stage your changes and commit them to your local repository:
     ```bash
     git add .
     git commit -am "Initial commit with project structure".
     ```

   **Explanation:**
   - `git add .` stages all changes for the next commit.
   - `git commit -am "Initial commit"` creates a commit with a message describing the changes.

5. **Push Your Changes:**

After making and committing your changes locally, the next step is to push those changes to your GitHub repository. 
This process updates the remote repository on GitHub with your latest changes.

### Command Explanation:

Use the following command to push your committed changes:

```bash
  git push origin main
```

This command comprises two main components:

- git push:
        The git push command is used to upload local changes to a remote repository, in this case, GitHub.
- origin main:
        The origin refers to the remote repository's alias. When you cloned your repository, Git automatically set up an alias called origin for the URL of the repository on GitHub.
        main represents the branch you are pushing to. In Git, the term "main" typically refers to the main branch of your repository, also known as the default branch.

What Happens When You Push:

- Staging Changes:
        Before pushing, ensure you have staged your changes using git add . and committed them using git commit -m "Your commit message". This prepares your changes for upload.

- Connecting to GitHub:
        Running git push establishes a connection to the GitHub repository using the origin alias.

- Uploading Changes:
        The changes you committed locally are uploaded to the remote repository on GitHub.

- Updating the Repository:
        The main branch on GitHub is updated with your latest changes, making your updated code accessible to others who may collaborate on the project.

You can find the name of your current branch (e.g., ```git branch```).

- Note:

    If you're working on a branch other than main, replace main with the name of your current branch.

    Always ensure that your local branch is up-to-date with the remote branch before pushing changes to avoid conflicts.

    You can ensure that GitHub Pages is enabled for the repository and that the source branch (e.g., main or master) is correctly configured.

Now, with your changes successfully pushed, others can view and collaborate on the updated codebase on GitHub.

6. **Visit Your Webpage:**
   - After a few minutes, your webpage will be live at `https://yourusername.github.io`.

## Testing Changes Locally

Before pushing changes to GitHub, you can test your webpage locally using Jekyll. Follow these steps:

1. **Install Ruby and Prerequisites:**
   - Run the following commands to install Ruby and prerequisites:
     ```bash
     sudo apt-get install ruby-full build-essential zlib1g-dev
     echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
     echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
     echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
     source ~/.bashrc
     gem install jekyll bundler
     ```

2. **Run Jekyll:**
   - Navigate to your local repository in the terminal.
   - Run the following command to start the Jekyll server:
     ```bash
     bundle exec jekyll serve
     ```

   **Note:**
   - If you encounter an error with Ruby 3.0 or later, try running `bundle add webrick` and then `bundle exec jekyll serve`.

3. **Preview Your Site:**
   - Open your web browser and go to [http://localhost:4000](http://localhost:4000) to preview your site.

## Usage

Simply open the `index.html` file in a web browser to view the webpage.

Feel free to explore the code, and if you have any suggestions or improvements, open an issue or submit a pull request!

Happy coding!

## Contribution

[See the contribution guide.](./CONTRIBUTING.md)

## Theme from Bootswatch

The theme used in this project is from [Bootswatch](https://bootswatch.com/), a collection of free themes for Bootstrap. You can explore different themes on the Bootswatch website to customize the look and feel of your Bootstrap-based project.
