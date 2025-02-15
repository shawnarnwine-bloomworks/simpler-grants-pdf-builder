# TODO

- add updated to NOFOs
- add status to NOFOs
- Write ADRs
  - Why Python
- Maybe: add Google login
- For deployed app, maybe logging?
- Password reset flow on command line
- Password reset flow exists
- Refac: short section names for breadcrumbs means we can loop
- Handle imagesinline in documents
- Theme variants
  - ACF white
  - HRSA variant
- Themes
  - ACL
- Maybe: include preceding paragraph in front of tables potentially
- Update the README
- Big cover page design
  - Blue large cover HRSA
  - White large cover HRSA
- PDF metadata as tags
- Add a way to change settings from the Django admin

# DONE

- Fix: Strip empty HTML tags so that NOFOs don't blow up on import
- Fix: Headings have less top spacing if they follow another heading
- Fix: Contact section is not a step
- Fix: spacing above table horizontal line
- New combined CDC and HHS logo
- Fix: use Nofo's real title
- Icons: re-do them
- Fix: header breadcrumbs can be out of order if order is not explicit
- Change body heading sizes to match typescale
- Fix: Show arrows on bolded li elements in table cells
- Fix: Use vibrant blue instead of dark for white CDC theme
- New callout box style + new PDF icon
- Fix: callout box headings are h5s
- Cover photo src set in view based on nofo number, else default
- Big cover page design
  - Blue large cover CDC
  - Add field to NOFO
- Let’s do that caption thing + add HR
- Double the space under tables
- Half the space under headings
- Don’t look at rows anymore for table sizing
- Application table for CDC white
- Single column for section 4 landscape
- Support for nested lists
  - Nested lists are not marked up by Google Docs
- Add new coach
- Fix: duplicate ids for headers being generated
- Fix: HTML validation
- Fix: Internal links are broken (eg, Questions callout box)
- Fix: editing borked for subsection
- Convert all the font sizes to pt
- Before you begin
  - Add icons
  - Move after ToC
  - Add to ToC
- Fix: Application table single cell layout for sublists
- Fix: extra whitespace in links
- Callout boxes
  - Put them after the summary
  - Create the Questions callout box
- Single cell tables are callout boxes
- Add tagline to NOFO
- Add subagency to NOFO
- Consolidate form generation macro
- Guess the opdiv, agency, subagency
- Watermark the image
- Broken on CDC
  - Heading level 7 omg
  - Lists inside of table cells
  - Too-long tables
  - Up/down arrow in list items in tables
  - Checklist icon in tables
  - Drop empty bullets
  - Lists in tables have way too much left padding
- Fix: NOFO title and number if nested in spans
- Guess application deadline
- Add a button to print the PDF
- Add Public Sans
- View page looks more like rendered NOFO
- Icons
  - Include on the section title pages
  - Include on the table of contents pages
- Fix: add new domain to settings
- Add favicon
- Fix: subsections showing up out of order in prod
- Add version number
- Before you start page
- Remove the extra blank page after the cover page
- Add floating view link to edit page
- Fix: duplicate ids for section pages and h2s
- Endnotes
- Switch logos per theme
- Theme variants
  - HRSA white
  - CDC white
- Fix the font sizes
  - Cover page portrait (HRSA)
  - Cover page landscape (CDC)
  - Table of contents (HRSA)
  - Table of contents (CDC)
  - Section title pages (CDC)
  - Section title pages (HRSA)
  - Content pages (HRSA)
  - Content pages (CDC)
- Table of contents
- Guess the theme
- Suggest the tagline
- Guess subsections that are callout boxes
- Tables on 2 column layout
- Themes
  - HRSA
  - CDC
  - ACF
- Add a theme to the NOFO
  - add to model
  - migrate
  - add an edit page
  - use to swap CSS file
- Add new coaches
- Suggest opportunity number when importing a NOFO
  - If number found, skip page
  - If number not found, manual assignment
  - Add to model + edit page
  - Add to nofo index and admin listing
- Add caption element to tables
- Write tests
  - Suggestion code
  - Section parsing code
  - Subsection parsing code
  - Table interpreting code
  - Build nofo code
  - Overwrite nofo code
  - Add header ids code
- Safelist incoming IPs for document viewing
- New running header
  - Running header knows what section it is
- Refac: clean up id generation for headers
- Use CSS vars for colours
- Fix the fonts
  - Get them to load at all
  - Make sure the headings show up
  - Add 2/3rds layout
- A11y scan for all pages
- Footer
  - Bottom left: section name
  - Bottom right: page number
- Write ADRs
  - Why DocRaptor
- Build a title page
  - Title of NOFO
  - HRSA logo
  - Refac: Big pic
  - HHS logo in the right colour
  - Refac: Opportunity number
- Build section pages
  - Title of section
  - Background colour
  - Links to H3s
  - Links to other sections
  - Full page colour
  - Counter for the page references
  - New stepped header
  - New stepped header knows what section it is
- Fix: Don't allow people to see account management pages unless logged in
- Force people who haven't ever logged in to reset password
- Remove old password from the edit password screen
- For deployed app, use Cloud Postgres
- Robots file
- For deployed app, set secure flags
- For deployed app, use domain for allowed domains
- Refac: Headers with top links
- Refac: Use section and div for all pages
- 404 page
- Refac: cleaner text inputs
- Refac: macro for (success) messages
- Update top nav with "current page" if on profile
- Change name
- Change password
  - Use type="password" for password field
- Remove 'documents' app
- Remove groups from Django admin
- Add second CSS file
- Add auth to pages
- Create login/logout flow
- Add accounts
- Clean up deployment
  - Prefer SQLite
- add datetime to NOFO creation
- consistent table column widths
- tables import without a header row
- add audit trail
- delete a NOFO
- add coach for nofos
  - add a coach to the nofo import flow
- preserve header ids on import
- floating section headers in edit view
- render the markdown in the edit screen
- re-import a previously imported NOFO
- allow empty markdown
- get the markdown editor working
- add 'order' for sections and subsections
- add tags for subsection
- edit the title
- fix: word breaks in the edit view
- remove 'posts' app
- create a view page
- add alert for succesful import
- predict the title
- add error messages
- index for all NOFOs
- import a NOFO
  - as HTML
  - as MD
- add black formatter
- saving works
- set up super basic edit flow
- styles the view
- styles the table
- styles the edit flow
- edit links in table
- back links on every page
- bring in the USWDS styles
- set up super basic view
- set up super basic table
- set up index view
- create 3 more as fixtures
- manually create something that looks like a nofo
- set up super basic schema
