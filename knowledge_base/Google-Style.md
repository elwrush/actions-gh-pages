Google HTML/CSS Style Guide

1\. Background

This document defines formatting and style rules for HTML and CSS. It aims at improving collaboration, code quality, and enabling supporting infrastructure. It applies to raw, working files that use HTML and CSS, including GSS files. Tools are free to obfuscate, minify, and compile as long as the general code quality is maintained.

2\. General

2.1 General Style Rules

Protocol

Use HTTPS for embedded resources where possible. Always use HTTPS (https:) for images and other media files, style sheets, and scripts, unless the respective files are not available over HTTPS.

Not recommended: omits protocol

<script src="//www.google.com/js/gweb/analytics/autotrack.js"></script>

Recommended

<script src="https://www.google.com/js/gweb/analytics/autotrack.js"\&gt;\&lt;/script>

2.2 General Formatting Rules

Indentation

Indent by 2 spaces at a time. Don’t use tabs or mix tabs and spaces for indentation.

Example HTML:

<ul>

<li>Fantastic

<li>Great

</ul>

Example CSS:

.example {

color: blue;

}

Capitalization

Use only lowercase. All code has to be lowercase: This applies to HTML element names, attributes, attribute values (unless text/CDATA), CSS selectors, properties, and property values (with the exception of strings).

Not recommended

<A HREF="/">Home</A>

Recommended

<a href="/">Home</a>

Not recommended (CSS)

color: #E5E5E5;

Recommended (CSS)

color: #e5e5e5;

Trailing Whitespace

Remove trailing white spaces. Trailing white spaces are unnecessary and can complicate diffs.

Not recommended

<p>What?\_

Recommended

<p>What?

2.3 General Meta Rules

Encoding

Use UTF-8 (no BOM). Make sure your editor uses UTF-8 as character encoding, without a byte order mark. Specify the encoding in HTML templates and documents via <meta charset="utf-8">. Do not specify the encoding of style sheets as these assume UTF-8.

Recommended

<meta charset="utf-8">

Comments

Explain code as needed, where possible. Use comments to explain code: What does it cover, what purpose does it serve, why is a respective solution used or preferred?

Action Items

Mark TODOs and FIXMEs with TODO(namelessone) (or similar). Only use TODO to highlight an action item. If you want to leave a note, strictly use NOTE.

3\. HTML

3.1 HTML Style Rules

Document Type

Use HTML5. HTML5 (HTML syntax) is preferred for all HTML documents: <!DOCTYPE html>.

HTML Validity

Use valid HTML where possible. Use valid HTML code unless that is not possible due to file size constraints or implementation guarantees.

Not recommended

<title>Test</title>

<article>This is only a test.

Recommended

<!DOCTYPE html>

<meta charset="utf-8">

<title>Test</title>

<article>This is only a test.</article>

Semantics

Use HTML according to its purpose. Use elements (sometimes incorrectly called "tags") for what they have been created for. For example, use heading elements for headings, p elements for paragraphs, a elements for anchors, etc.

Multimedia Fallback

Provide alternative contents for multimedia. For multimedia, such as images, videos, animated objects via canvas, make sure to offer alternative access. For images that means use of meaningful alternative text (alt); for video and audio transcripts and captions, if available.

Not recommended

<img src="spreadsheet.png">

Recommended

<img src="spreadsheet.png" alt="Spreadsheet screenshot.">

Separation of Concerns

Separate structure from presentation and behavior. Strictly keep structure (markup), presentation (styling), and behavior (scripting) apart, and try to keep the interaction between the three to a minimum.

Entity References

Do not use entity references. There is no need to use entity references like \&mdash;, \&rdquo;, or \&#x263a;, assuming the same encoding (UTF-8) is used for files and the editor.

Not recommended

The currency symbol for the Euro is "\&eur;".

Recommended

The currency symbol for the Euro is "€".

Optional Tags

Omit optional tags (optional). For file size optimization and scannability purposes, consider omitting optional tags. The HTML5 specification defines what tags can be omitted.

Not recommended

<!DOCTYPE html>

<html>

<head>

<title>Spending money</title>

</head>

<body>

<p>Spending money.</p>

</body>

</html>

Recommended

<!DOCTYPE html>

<title>Spending money</title>

<p>Spending money.

type Attributes

Omit type attributes for style sheets and scripts. Do not use type attributes for style sheets (unless not using CSS) and scripts (unless not using JavaScript).

Not recommended

<link rel="stylesheet" href="//www.google.com/css/maia.css" type="text/css">

Recommended

<link rel="stylesheet" href="//www.google.com/css/maia.css">

3.2 HTML Formatting Rules

HTML Quotation Marks

Use double quotation marks for attributes. Use double ("") rather than single ('') quotation marks around attribute values.

Not recommended

<a class='maia-button maia-button-secondary'>Sign in</a>

Recommended

<a class="maia-button maia-button-secondary">Sign in</a>

4\. CSS

4.1 CSS Style Rules

CSS Validity

Use valid CSS where possible. Unless dealing with CSS validator bugs or requiring proprietary syntax, use valid CSS code.

ID and Class Naming

Use meaningful or generic ID and class names. Instead of presentational or cryptic names, always use ID and class names that reflect the purpose of the element in question, or that are otherwise generic.

Not recommended: meaningless

\#yee-1901 {}

Not recommended: presentational

.button-green {}

.clear {}

Recommended: specific

\#gallery {}

\#login {}

.video {}

Recommended: generic

.aux {}

.alt {}

ID and Class Name Style

Use ID and class names that are as short as possible but as long as necessary.

Not recommended

\#navigation {}

.atr {}

Recommended

\#nav {}

.author {}

Type Selectors

Avoid qualifying ID and class names with type selectors. Unless necessary (for example with helper classes), do not use element names in conjunction with IDs or classes.

Not recommended

ul#example {}

div.error {}

Recommended

\#example {}

.error {}

Shorthand Properties

Use shorthand properties where possible. CSS offers a variety of shorthand properties (like font) that should be used whenever possible, even in cases where only one value is explicitly set.

Not recommended

border-top-style: none;

font-family: palatino, georgia, serif;

font-size: 100%;

line-height: 1.6;

padding-bottom: 2em;

padding-left: 1em;

padding-right: 1em;

padding-top: 0;

Recommended

border-top: 0;

font: 100%/1.6 palatino, georgia, serif;

padding: 0 1em 2em;

0 and Units

Omit unit specification after "0" values. Do not use units after 0 values unless they are required.

Example

margin: 0;

padding: 0;

Leading 0s

Omit leading "0"s in values. Do not use put 0s in front of values or lengths between -1 and 1.

Example

font-size: .8em;

Hexadecimal Notation

Use 3 character hexadecimal notation where possible. For color values that permit it, 3 character hexadecimal notation is shorter and more succinct.

Not recommended

color: #eebbcc;

Recommended

color: #ebc;

Prefixes

Prefix selectors with an application-specific prefix (optional). In large projects as well as for code that gets embedded in other projects or on external sites use prefixes for id and class names. Use short, unique identifiers followed by a dash.

Example

.adw-help {} /\* AdWords /

.maia-note {} / Maia \*/

ID and Class Name Delimiters

Separate words in ID and class names by a hyphen. Do not concatenate words and abbreviations in selectors by any characters (including none at all) other than hyphens, in order to improve understanding and scannability.

Not recommended

.demoimage {}

.error\_status {}

Recommended

.demo-image {}

.error-status {}

Hacks

Avoid user agent detection as well as CSS "hacks" - try a different approach first.

4.2 CSS Formatting Rules

Declaration Order

Alphabetize declarations. Put declarations in alphabetical order in order to achieve consistent code in a way that is easy to remember and maintain.

Example

background: fuchsia;

border: 1px solid;

-moz-border-radius: 4px;

-webkit-border-radius: 4px;

border-radius: 4px;

color: black;

text-align: center;

text-indent: 2em;

Block Content Indentation

Indent all block content. Indent all block content, that is rules within rules as well as declarations, so to reflect hierarchy and improve understanding.

Example

@media screen, projection {

html {

background: #fff;

color: #444;

}

}

Declaration Stops

Use a semicolon after every declaration. End every declaration with a semicolon for consistency and extensibility reasons.

Not recommended

.test {

display: block;

height: 100px

}

Recommended

.test {

display: block;

height: 100px;

}

Property Name Stops

Use a space after a property name's colon. Always use a single space between property and value (but no space between property and colon) for consistency reasons.

Not recommended

h3 {

font-weight:bold;

}

Recommended

h3 {

font-weight: bold;

}

Declaration Block Separation

Use a space between the last selector and the declaration block. Always use a single space between the last selector and the opening brace that begins the declaration block.

Not recommended

\#video{

margin-top: 1em;

}

Recommended

\#video {

margin-top: 1em;

}

Selector and Declaration Separation

Separate selectors and declarations by new lines. Always start a new line for each selector and declaration.

Not recommended

a:focus, a:active {

position: relative; top: 1px;

}

Recommended

h1,

h2,

h3 {

font-weight: normal;

line-height: 1.2;

}

Rule Separation

Separate rules by new lines. Always put a blank line (two line breaks) between rules.

Example

html {

background: #fff;

}

body {

margin: auto;

width: 50%;

}

CSS Quotation Marks

Use single quotation marks for attribute selectors and property values. Use single ('') rather than double ("") quotation marks for attribute selectors or property values. Do not use quotation marks in URI values (url()).

Not recommended

@import url("https://www.google.com/css/maia.css");

html {

font-family: "open sans", arial, sans-serif;

}

Recommended

@import url(https://www.google.com/css/maia.css);

html {

font-family: 'open sans', arial, sans-serif;

}

4.3 CSS Meta Rules

Section Comments

Group sections by a section comment.

Example

/\* Header \*/

\#adw-header {}

/\* Footer \*/

\#adw-footer {}

/\* Gallery \*/

.adw-gallery {}

Parting Words

Be consistent.

If you’re editing code, take a few minutes to look at the code around you and determine its style. If they use spaces around all their arithmetic operators, you should too. If their comments have little boxes of asterisks around them, make your comments have little boxes of asterisks around them too.

The point of having style guidelines is to have a common vocabulary of coding so people can concentrate on what you’re saying rather than on how you’re saying it. We present global style rules here so people know the vocabulary, but local style is also important. If code you add to a file looks drastically different from the existing code around it, it throws readers out of their rhythm when they go to read it. Avoid this.

