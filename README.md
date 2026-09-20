---
permalink: /about/
---
# JetBrains IDE Release Dates

[![All Contributors](https://img.shields.io/github/all-contributors/ChrisCarini/jetbrains-ide-release-dates?color=ee8449&style=flat-square)](#contributors)

## Description

The intent of this repository is to capture the actual release dates for JetBrains IDEs. The concept stems from a wiki
page at work which was created to help our team plan work around the potential release dates of JetBrains IntelliJ IDEA.

_**Why** did our team care?_ Well, we develop and maintain an ecosystem around JetBrains (from internal-only plugin
distribution, to license management, to a custom distributed IntelliJ IDE). Knowing when a release might come allows us
to better plan our week / month / year to enable our developers to be as productive as possible!

Very simply, the idea here is to allow one to more accurately predict (we used to just guess months out - turns out,
that's very inaccurate) about when a particular IntelliJ IDEA release ***may*** occur based on historical data.

## Website and previews

The Jekyll website renders the existing Markdown histories directly; the release-date fetcher and its data format are
unchanged. It includes a product directory, horizontally scrollable release tables, and archived edition histories.

**Recommended: preview locally first, then review the PR's downloadable preview before publishing.** Neither option
requires enabling GitHub Pages, and merging this setup does not publish the site automatically.

### Preview locally

With Ruby 3.3 and Bundler installed, run these commands from the repository root:

```shell
bundle install
bundle exec jekyll serve
```

Open <http://127.0.0.1:4000/jetbrains-ide-release-dates/>. Jekyll rebuilds when you edit site files; restart it after
changing `_config.yml`. This uses the same project subpath as production, so you can check navigation and styling.
For a build without starting a server, run `bundle exec jekyll build`.

### Preview a pull request

The **Site preview / Build and preview** check builds both the production configuration and a standalone preview on
each PR, including fork PRs. It also runs on pushes to `main` and can be run manually from the Actions tab once the
workflow is on the default branch. GitHub may require maintainer approval before running a first-time contributor's workflow.

1. Open the PR's **Checks** tab and follow the **Site preview** workflow to its run summary.
2. Download the **site-preview** artifact (GitHub sign-in required; retained for 14 days).
3. Extract the ZIP and, from the extracted folder containing `index.html`, run:

   ```shell
   python3 -m http.server 8000 --bind 127.0.0.1
   ```

4. Open <http://127.0.0.1:8000/>. No Ruby installation is needed for an artifact preview.

Do not double-click the HTML files: their links and assets require an HTTP server. The preview uses an empty base path
for convenient local serving; the production build separately checks the configured `/jetbrains-ide-release-dates` path.
PR builds have read-only repository access, no deployment permissions, and never overwrite the live site.

GitHub Pages does not provide built-in isolated PR preview URLs. Artifacts are the simplest GitHub-only option that
keeps unpublished changes off the live site. If clickable, remotely hosted previews become necessary, a separate service
such as Cloudflare Pages or Netlify can provide isolated deploy previews, but requires an additional integration.

### Publish when ready

Nothing has to be published to use the previews. After reviewing them:

1. Merge the site and workflows to `main`.
2. In **Settings → Pages → Build and deployment**, choose **GitHub Actions** as the source (not deployment from a branch).
3. In **Settings → Environments → github-pages**, restrict deployment branches to `main`. Optionally require a reviewer
   for an additional approval before each publication, where supported.
4. Run **Actions → Deploy GitHub Pages → Run workflow**, selecting `main`. This explicitly publishes the site to
   <https://chriscarini.github.io/jetbrains-ide-release-dates/>.

By default, publication is manual; merging a PR or updating release data will not republish it. After launch, you can
optionally set the repository Actions variable **`PAGES_AUTO_DEPLOY`** to **`true`** under
**Settings → Secrets and variables → Actions → Variables**. This enables deployments on pushes to `main` and successful
completions of **JetBrains IDE Release Date Fetcher** on `main`. The latter is necessary because commits pushed by
`GITHUB_TOKEN` do not trigger another push workflow. Production always builds `main`, never a PR's code or artifacts.
Remove the variable or set it to `false` to return to manual publication; this does not unpublish an existing site.

## JetBrains IDEs

- [AppCode](ides/AppCode_Release_Dates.md)
- [CLion](ides/CLion_Release_Dates.md)
- [GoLand](ides/GoLand_Release_Dates.md)
- [IntelliJ IDEA](ides/IntelliJ_IDEA_Release_Dates.md)
  - **Note:** As of 2025.3 (released on 2025-12-08), _["there is one IntelliJ IDEA, replacing the separate IntelliJ IDEA Community Edition and IntelliJ IDEA Ultimate to keep things simple and convenient"](https://blog.jetbrains.com/idea/2025/12/intellij-idea-unified-release/)_.
- [PhpStorm](ides/PhpStorm_Release_Dates.md)
- [PyCharm](ides/PyCharm_Release_Dates.md)
- [ReSharper C++](ides/ReSharper_C%2B%2B_Release_Dates.md)
- [ReSharper](ides/ReSharper_Release_Dates.md)
- [Rider](ides/Rider_Release_Dates.md)
- [RubyMine](ides/RubyMine_Release_Dates.md)
- [RustRover](ides/RustRover_Release_Dates.md)
- [WebStorm](ides/WebStorm_Release_Dates.md)

## Other JetBrains Products

- [Floating License Server](ides/Floating_License_Server_Release_Dates.md)
- [Gateway (Remote Development)](ides/Gateway_Release_Dates.md)
- [IDE Services](ides/IDE_Services_Release_Dates.md)
- [Mono Font](ides/Mono_Font_Release_Dates.md)
- [Toolbox App](ides/Toolbox_App_Release_Dates.md)

## Frequently Asked Questions (FAQ)

### **Question:** What about `IntelliJ IDEA Community Edition` and `PyCharm Community Edition`?

**Answer:** These two IDEs have identical release cadences with the respective paid versions.

- IntelliJ IDEA Community Edition (see [IntelliJ IDEA Ultimate](ides/IntelliJ_IDEA_Ultimate_Release_Dates.md) - release
  dates
  identical as of 2021-01-01.)
- PyCharm Community Edition (see [PyCharm Professional Edition](ides/PyCharm_Professional_Edition_Release_Dates.md) -
  PyCharm Pro has
  a longer release history, with otherwise identical release dates.)
  - *Note(s):*
    - Prior to 2025.1, PyCharm Community and PyCharm Professional Edition were different IDEs. They have merged into one as of the 2025.1 release on 2025-04-16.
    - See JetBrains' blog post ["PyCharm, the Only Python IDE You Need"](https://blog.jetbrains.com/pycharm/2025/04/unified-pycharm/) for details.
    - See [PyCharm Professional Edition](ides/PyCharm_Professional_Edition_Release_Dates.md) for the old file (which automation will no longer update).

## Obtaining Release Dates

The release dates in the markdown files of this repository are automatically obtained from a JetBrains API.

Prior to 2021, they were manually obtained and updated in this repo by:

<table>
  <tr>
    <td align="center"><a href="https://github.com/ChrisCarini"><img src="https://avatars2.githubusercontent.com/u/6374067?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Chris Carini</b></sub></a></td>
    <td align="center"><a href="https://github.com/baron1405"><img src="https://avatars2.githubusercontent.com/u/989635?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Baron Roberts</b></sub></a></td>
    <td align="center"><a href="https://github.com/vicky17d"><img src="https://avatars2.githubusercontent.com/u/1669024?v=4?s=100" width="100px;" alt=""/><br /><sub><b>vicky17d</b></sub></a></td>
  </tr>
</table>

See our [Obtaining Release Dates](docs/Obtaining%20Release%20Dates.md) document for some suggestions on methodology for
how we previously obtained release dates for previous IDE versions.

## Developing Quick Start

The below commands will get the basic setup for developing on the Python module which does the fetching of IDE release
data and generation of the Markdown files.

```shell
cd release_date_fetcher
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python generate_markdown_files.py
```

## Contributing

We love contributions! See our [CONTRIBUTING](docs/CONTRIBUTING.md) file for more information.

## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/ChrisCarini"><img src="https://avatars.githubusercontent.com/u/6374067?v=4?s=100" width="100px;" alt="Chris Carini"/><br /><sub><b>Chris Carini</b></sub></a><br /><a href="#bug-ChrisCarini" title="Bug reports">🐛</a> <a href="#code-ChrisCarini" title="Code">💻</a> <a href="#doc-ChrisCarini" title="Documentation">📖</a> <a href="#example-ChrisCarini" title="Examples">💡</a> <a href="#ideas-ChrisCarini" title="Ideas, Planning, & Feedback">🤔</a> <a href="#maintenance-ChrisCarini" title="Maintenance">🚧</a> <a href="#question-ChrisCarini" title="Answering Questions">💬</a> <a href="#review-ChrisCarini" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://www.cthing.com"><img src="https://avatars.githubusercontent.com/u/989635?v=4?s=100" width="100px;" alt="Baron Roberts"/><br /><sub><b>Baron Roberts</b></sub></a><br /><a href="#code-baron1405" title="Code">💻</a> <a href="#ideas-baron1405" title="Ideas, Planning, & Feedback">🤔</a> <a href="#maintenance-baron1405" title="Maintenance">🚧</a> <a href="#review-baron1405" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/vicky17d"><img src="https://avatars.githubusercontent.com/u/1669024?v=4?s=100" width="100px;" alt="vicky17d"/><br /><sub><b>vicky17d</b></sub></a><br /><a href="#code-vicky17d" title="Code">💻</a> <a href="#maintenance-vicky17d" title="Maintenance">🚧</a> <a href="#review-vicky17d" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/opticyclic"><img src="https://avatars.githubusercontent.com/u/1222693?v=4?s=100" width="100px;" alt="opticyclic"/><br /><sub><b>opticyclic</b></sub></a><br /><a href="#content-opticyclic" title="Content">🖋</a> <a href="#example-opticyclic" title="Examples">💡</a> <a href="#ideas-opticyclic" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/gehbiszumeis"><img src="https://avatars.githubusercontent.com/u/16896724?v=4?s=100" width="100px;" alt="gehbiszumeis"/><br /><sub><b>gehbiszumeis</b></sub></a><br /><a href="#code-gehbiszumeis" title="Code">💻</a> <a href="#content-gehbiszumeis" title="Content">🖋</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
