<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GNU v3.0 License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<br />
<div align="center">
  <a href="https://github.com/Pobl-Group/mould-analysis">
    <img src="assets/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Mould Analysis</h3>

  <p align="center">
    A tool for assessing whether a job description contains an exact or partial match for key words associated with damp or mould.
    <br />
    <a href="https://github.com/Pobl-Group/mould-analysis/issues">Report Bug</a>
    ·
    <a href="https://github.com/Pobl-Group/mould-analysis/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About the Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About the Project

This tool was designed to allow us to find damp and mould related words within job descriptions. When provided with a job description, the algorithm will return a series of scores that indicate whether there is a word in the description that is an exact or partial match for the one of keywords provided.
We have included the ability to adjust the keywords that are searched for to suit your organisation’s needs. We also allow for the removal of “stop words” which are words that are to be removed from job descriptions to prevent instances of false positives.

**Note:** where an exact match is not found, the scores can only say that there *might* be a match. Like many algorithms, there is a trade off between being too precise (and reducing false positives as much as possible) and flexible enough to be useful (and capture instances where our confidence level might be slightly lower). To get the most out of the algorithm, we suggest experimenting by altering the key words and stop words and then examining the scores returned to check that the configuration works for your organisation.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

- [Python][python-url]
- A CSV dataset containing just two fields: `job_id` and `description`.


### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Pobl-Group/mould-analysis.git
   ```
1. Install packages
   ```sh
   pip install -r requirements.txt
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

### Data preparation
The best way to use this tool, is to provide one row per job and to assemble a description by combining all known descriptions for that job into one. For example, a job may involve multiple tasks and so, you may wish to combine the overall job description with the descriptions of each task related to that job.

It is worth noting that before producing the scores, the program will first standardise the descriptions by converting them to lower case and removing punctuation, numbers and extra spaces.

### Key words
You need to specify a set of lower case keywords that would suggest the job is related to damp or mould. You should try to pick words that are only used when describing a job to remedy damp or mould. Besides from the obvious inclusion of “damp” and “mould”, consider adding names of treatments or tasks associated with removing damp and mould.

### Stop words
To reduce false positives, it is a good idea to remove certain words from the job descriptions to make the scoring process as reliable as possible. There may be words that are similar to a key word but that have different meanings, like “moulding” which may be unlikely to feature as a description of mould in a property but might be used to describe the fact that the mouldings around a window are cracked.

### The Scores
Once the program has run, several scores will be produced.

**one_to_one_ratio:** this is a simple ratio score from “thefuzz” library. It checks the similarity between each of the words in the description with each of the key words. After these comparisons are made, the highest score is returned.  The higher the score, the better the match there is between a key word and a word in the description. A score of 100 represents an exact match.

**set_ratio:** this is the partial token set ratio from “thefuzz” library. This function appears to have been deprecated in the latest version of thefuzz but we have left this in place for you to examine the output.

**min_levenshtien_score:** this is the minimum levenshtien distance found when comparing each word in the job description with each of the keywords. The levenshtien distance is essentially a measure of the number of steps required to change one word to another. This also known as the “edit distance”. Unlike the other scores, the lower the levenshtien distance the better.

**simple_search:** this is a simple comparison between each word in the description and each of the keywords. It will return a score of 100 when an exact match is found, otherwise it will return a score of 0.

**best_score:** this is the best score returned out of the one_to_one_ratio, set_ratio and simple_search.

### Interpreting the scores
We suggest you examine the output and familiarise yourself with the scores returned. We have used the one_to_one ratio score and the simple search scores mostly. We have chosen to view a one_to_one score of 85 or higher as a suitable match for a key word, however you may wish to adjust this based on your needs.


<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the GNU General Public License v3.0. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [pandas](https://pypi.org/project/pandas/)
* [thefuzz](https://pypi.org/project/thefuzz/)
* [Levenshtein](https://pypi.org/project/Levenshtein/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Pobl-Group/mould-analysis.svg?style=for-the-badge
[contributors-url]: https://github.com/Pobl-Group/mould-analysis/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Pobl-Group/mould-analysis.svg?style=for-the-badge
[forks-url]: https://github.com/Pobl-Group/mould-analysis/network/members
[stars-shield]: https://img.shields.io/github/stars/Pobl-Group/mould-analysis.svg?style=for-the-badge
[stars-url]: https://github.com/Pobl-Group/mould-analysis/stargazers
[issues-shield]: https://img.shields.io/github/issues/Pobl-Group/mould-analysis.svg?style=for-the-badge
[issues-url]: https://github.com/Pobl-Group/mould-analysis/issues
[license-shield]: https://img.shields.io/github/license/Pobl-Group/mould-analysis.svg?style=for-the-badge
[license-url]: https://github.com/Pobl-Group/mould-analysis/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/company/pobl-group
[python-url]: https://www.python.org/
