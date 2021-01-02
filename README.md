# JetBrains IDE Release Dates

## Description

The intent of this repository is to capture the actual release dates for JetBrains IDEs. The concept stems from a wiki
page at work which was created to help our team plan work around the potential release dates of JetBrains IntelliJ IDEA.

_**Why** did our team care?_ Well, we develop and maintain an ecosystem around JetBrains (from internal-only plugin
distribution, to license management, to a custom distributed IntelliJ IDE). Knowing when a release might come allows us
to better plan our week / month / year to enable our developers to be as productive as possible!

Very simply, the idea here is to allow one to more accurately predict (we used to just guess months out - turns out,
that's very inaccurate) about when a particular IntelliJ IDEA release ***may*** occur based on historical data.

## JetBrains IDEs

- [AppCode](ides/AppCode_Release_Dates.md)
- [CLion](ides/CLion_Release_Dates.md)
- [GoLand](ides/GoLand_Release_Dates.md)
- [IntelliJ IDEA Ultimate](ides/IntelliJ_IDEA_Ultimate_Release_Dates.md)
- [PyCharm Professional Edition](ides/PyCharm_Professional_Edition_Release_Dates.md)
- [PhpStorm](ides/PhpStorm_Release_Dates.md)
- [ReSharper C++](ides/ReSharper_C%2B%2B_Release_Dates.md)
- [Rider](ides/Rider_Release_Dates.md)
- [RubyMine](ides/RubyMine_Release_Dates.md)
- [ReSharper](ides/ReSharper_Release_Dates.md)
- [WebStorm](ides/WebStorm_Release_Dates.md)

## Frequently Asked Questions (FAQ)

### **Question:** What about `IntelliJ IDEA Community Edition` and `PyCharm Community Edition`?

**Answer:** These two IDEs have identical release cadences with the respective paid versions.

- IntelliJ IDEA Community Edition (see [IntelliJ IDEA Ultimate](ides/IntelliJ_IDEA_Ultimate_Release_Dates.md) - release dates
  identical as of 2021-01-01.)
- PyCharm Community Edition (see [PyCharm Professional Edition](ides/PyCharm_Professional_Edition_Release_Dates.md) - PyCharm Pro has
  a longer release history, with otherwise identical release dates.)

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