# Qwen2.5-1.5B Finance QA
 
[financial-Qwen2.5-1.5B](https://huggingface.co/YoussefEldoksh/financial-Qwen2.5-1.5B-Instruct) is a fine-tuned version of [Qwen2.5-1.5B](https://huggingface.co/unsloth/Qwen2.5-1.5B-Instruct) for financial question answering, built to make learning finance concepts easier for students and beginners.
 
> **Disclaimer:** This model is for educational purposes only. It can produce incorrect or outdated information, including made-up figures. It is not financial advice and should not be used to make investment decisions.
 
## Overview
 
General-purpose language models often answer finance questions in a way that is either too shallow or too jargon-heavy for someone learning the subject. This project fine-tunes a small, efficient model to explain financial concepts clearly and answer common finance questions accurately, while staying light enough to run on modest hardware.
 
**What it can do**
- Explain core concepts (e.g. compound interest, P/E ratio, diversification, inflation)
- Answer factual and conceptual finance questions
- Break down terminology in plain language
## Model Details
 
| | |
|---|---|
| **Base model** | Qwen2.5-1.5B |
| **Fine-tuning method** | `[LoRA]` |
| **Dataset** | `[Josephgflowers/Finance-Instruct-500k]` |
| **Training examples** | `[423895 examples after filtering to only english examples]` |
| **Framework** | `[Transformers / trl / Unsloth / pandas]` |
| **Hardware** | `[1x A100 GPU on Google Colab]` |
| **Weights** | `[https://huggingface.co/unsloth/Qwen2.5-1.5B-Instruct]` |
 
## Quick Start
 
### Installation
 
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```
 
 
### Example
 
**Prompt:** What is compound interest?
 
**Response:** 

```
Compound interest is the interest calculated on the initial principal and also on any accumulated interest of a deposit or loan. It's the process
where you earn interest not only on your original investment, but also on the previously accrued interest that has grown over time.

The formula for compound interest can be expressed as:

A = P (1 + r/n)^(nt)

Where:
A is the future value of the investment/loan or deposit
P is the principal amount (the initial amount you invest or borrow)
r is the annual interest rate (in decimal form, so 4% would be .04)
n is the number of times that interest is compounded per year
t is the time your money is invested or borrowed for

The more often the interest is compounded, the faster the balance grows. This can make a significant difference over long periods of time.

Compound interest is an important concept to understand when it comes to saving and investing. By understanding how compound interest works, you can
plan for your financial future and make better decisions about where and how to invest your money.
``` 
## Limitations
 
- **Small model:** at 1.5B parameters, it can hallucinate facts, numbers, and calculations.
- **Knowledge cutoff:** it has no access to live market data, current prices, or recent regulations.
- **Not personalised advice:** it does not know your financial situation.
- **Domain coverage:** performance depends on the topics covered in the training data.
Always verify important information against reliable sources.


## Contact
 
`[Youssef Eldoksh]` · `[youssefeldoksh788@gmail.com]`
 