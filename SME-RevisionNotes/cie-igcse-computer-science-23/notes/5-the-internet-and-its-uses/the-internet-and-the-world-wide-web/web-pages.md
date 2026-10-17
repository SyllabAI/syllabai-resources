---
note_id: "rn_Gkfs8XrfGCnnYKgR"
title: "Web Pages"
source: https://www.savemyexams.com/igcse/computer-science/cie/23/revision-notes/5-the-internet-and-its-uses/the-internet-and-the-world-wide-web/web-pages
path: 5-the-internet-and-its-uses/the-internet-and-the-world-wide-web/web-pages
updated_at: "2024-09-09T09:56:54.095Z"
spec_point_ids: ["spcpt_wTgsPXB7QQRrtHCW", "spcpt_qSQ4tHvsYZqdZjbH", "spcpt_dCKf2Tn4VCFcTM2S", "spcpt_9VDfN9KR84nMPkTN", "spcpt_nSTxdp7RVp3cCYST"]
spec_point_codes: []
guided_study: false
---

# Web Pages

## Loading a Web Page

> **Spec point** — `spcpt_wTgsPXB7QQRrtHCW` · "4 Explain the purpose and functions of a web
browser
5 Describe how web pages are located, retrieved
and displayed on a device when a user enters a
URL"

## Loading a Web Page

### How is a web page loaded?

- Web pages** are held on web servers** (1), known as '**hosting**'
- To access a web page on a web server, **a web browser is used**
- In the browser, a user enters** a web page URL** (2)
- The browser sends the **domain name** to a **DNS **(3)
- The browser connects to the web server and **requests to access the page**
- **HTML **(4) is transferred and **rendered by the browser**, displaying the web page

## Web Servers

> **Spec point** — `spcpt_qSQ4tHvsYZqdZjbH` · "4 Explain the purpose and functions of a web
browser
5 Describe how web pages are located, retrieved
and displayed on a device when a user enters a
URL"

## Web Servers (1)

### What is a web server?

- A web server is **a remote computer** that **stores the files needed to display a web page** on the Internet
- Web servers are generally **available 24/7** and **security is managed** by the owner of the hardware
- Web servers provide access to **multiple users at the same time**

## Uniform Resource Locator (URL)

> **Spec point** — `spcpt_dCKf2Tn4VCFcTM2S` · 2 Understand what is meant by a uniform resource locator (URL)

## Uniform Resource
Locator (URL) (2)

### What is a URL?

- A **Uniform Resource Locator** (URL) is a** unique identifier** for a web page, known as the **website address **
- It is **text based** to make it easier to remember
- A user **enters a URL** into a web browser to view a web page
- An example of a URL is:

[https://www.savemyexams.com/igcse/computer-science/cie/23/revision-notes/](https://www.savemyexams.com/igcse/computer-science/cie/23/revision-notes/)

- A URL can typically be split into three parts:

  - **Protocol**
  - **Domain name**
  - **Web page/file name**
- Using the example about the URL would be split as follows:

| Protocol | https | Communication method to transfer data between client and server |
|---|---|---|
| Domain name | www.savemyexams.com | Name of the server where the resource is located |
| Web page/file name | /igcse/computer-science/cie/23/revision-notes/ | Location of the file or resources on the server |

## Domain Name System (DNS)

> **Spec point** — `spcpt_9VDfN9KR84nMPkTN` · "4 Explain the purpose and functions of a web
browser
5 Describe how web pages are located, retrieved
and displayed on a device when a user enters a
URL"

## Domain Name System (DNS) (3)

### What is a DNS?

- The Domain Name System (DNS) can be thought of as the Internet's equivalent to a **phone book**
- It is essentially a directory of domain names and is used to translate human-readable domain names to the numeric  **IP addresses **that computers use
- When you type a URL into your browser, **the DNS translates the domain name into its associated IP address** so your computer can connect to the server hosting the website
- Without DNS, we would have to remember the IP address of every site we want to visit

## HTML

> **Spec point** — `spcpt_nSTxdp7RVp3cCYST` · "4 Explain the purpose and functions of a web
browser
5 Describe how web pages are located, retrieved
and displayed on a device when a user enters a
URL"

## HTML (4)

### What is HTML?

- Hypertext Markup Language (**HTML**), is the foundational language **used to structure  and present content on the web**
- HTML consists of a series of elements, often referred to as "**tags**"
- Most tags are **opened and closed e.g. **`<html>` and `</html>`,` `whereas **some tags are only opened e.g. **`<img>` and `<link>`

#### Structure

- HTML is used to **define the basic structure of a webpage** by organising content into **sections **such as headers, paragraphs, and footers
- The `<html>` tag is the **root element** of an HTML page and includes all other HTML elements used to create a page structure

- In this example, HTML is used to create a structure with a **header**, two sections in the **main body**, and a **footer**
- Other examples of HTML being used for structure include:

  - **Creating lists to structure information**
  - **Positioning of text on the screen**
  - **Embedding media and interactive elements**

#### Present

- HTML is also used to **present and display information in a visually** meaningful way
- The content layer of a web page is made up of HTML elements such as **headings **(`<h1>, <h2>`, etc.), **paragraphs **(`<p>`), **links **(`<a>`), **images **(`<img>`), and more
- This layer is mainly handled by **CSS **(Cascading Style Sheets)

- In this example, **headings **(`<h1>`, `<h2>`) and** text formatting** tags (`<strong>`, `<em>`) are used to present the content clearly and with emphasis
- Other examples of HTML being used to present information include:

  - **Presenting data in a table**
  - **Displaying images with captions**

> **Worked Example**
> A company sells products over the Internet.
> 
> Explain how the information stored on the company’s website is requested by the customer, sent to the customer’s computer and displayed on the screen.
> 
> **[7]**
> 
> **Answer**
> 
> **Seven **from:
> 
> **Requested **
> 
> - **a web browser is used**
> - **user enters the URL / web address (into the address bar) // clicks a link containing the web address // clicks an element of the webpage**
> - **the URL / web address specifies the protocol**
> - **protocols used are Hyper Text Transfer Protocol (HTTP) / Hyper Text Transfer Protocol Secure (HTTPS) **
> 
> **Sent **
> 
> - **the URL / web address contains the domain name**
> - **the domain name is used to look up the IP address of the company**
> - **the domain name server (DNS) stores an index of domain names and IP addresses**
> - **web browser sends a request to the web server / IP address **
> 
> **Received**
> 
> - **Data for the website is stored on the company’s web server**
> - **webserver sends the data for the website back to the web browser**
> - **web server uses the customer’s IP address to return the data**
> - **the data is transferred into Hyper Text Mark-up Language (HTML)**
> - **HTML is interpreted/rendered by the web browser (to display the website)**
