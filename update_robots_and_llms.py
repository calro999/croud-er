# -*- coding: utf-8 -*-
import os

robots_content = """User-agent: *
Allow: /
Sitemap: https://haitoku.pages.dev/sitemap.xml

# ========================================================
# Search Engines & Standard Crawlers
# ========================================================
User-agent: Googlebot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: Bingbot
Allow: /

User-agent: DuckDuckBot
Allow: /

User-agent: DuckDuckGo-Favicons-Bot
Allow: /

User-agent: Yandex
Allow: /

User-agent: Applebot
Allow: /

User-agent: Applebot-Extended
Allow: /

User-agent: Baiduspider
Allow: /

User-agent: Yahoo! Slurp
Allow: /

# ========================================================
# AI Search, Agents & LLM Knowledge Base Crawlers
# ========================================================
# OpenAI / ChatGPT / SearchGPT
User-agent: GPTBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: OAI-SearchBot
Allow: /

# Anthropic / Claude
User-agent: ClaudeBot
Allow: /

User-agent: Claude-Web
Allow: /

User-agent: Anthropic-AI
Allow: /

# Perplexity AI
User-agent: PerplexityBot
Allow: /

# Meta / Facebook AI
User-agent: Meta-ExternalAgent
Allow: /

User-agent: FacebookBot
Allow: /

# ByteDance / TikTok AI
User-agent: Bytespider
Allow: /

# Mistral AI
User-agent: MistralAI-Bot
Allow: /

# Cohere AI
User-agent: cohere-ai
Allow: /

# Amazon Alexa & AI
User-agent: Amazonbot
Allow: /

# Common Crawl (Foundation for training all modern LLMs)
User-agent: CCBot
Allow: /

# Diffbot
User-agent: Diffbot
Allow: /
"""

with open("public/robots.txt", "w", encoding="utf-8") as f:
    f.write(robots_content)

print("Updated public/robots.txt with comprehensive AI/LLM & Search Engine crawler rules.")
