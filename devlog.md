# 12-21-2024
Design decisions about program flow and enforced input structure and plan for new user config (optional) and mix.-in feature for referencing prior audio files and bg tracks without having to include them in input dir within program operant directory.
 

# 12-22-2024
Switch dev environment to ubuntu vm and sublime text. Organization of new design necessitated deleting first attempt at structuring project in favor of OOP and starting with implementation priorities (i.e. defining test casses for class structure of mixer).

Starting point is skeleton of automated mixer main class -- sure to evolve, but basic entry point. Outlined basic steps for initializing the automixer as a blueprint for dev stages. Using branch am_class_structure and subbranch to tackle error reporting (top priority).

Otlined error reporting tests, error class (handler) structure and success/fail, and dev_mode reporting. Designing before bed is fun even if I save the code for another day :)

# 12-23-2024
Decided to pt error handling on backburner as qol feature and focus on main functionality first. Made progress on initial validation of active dir and subdir for bundled subs, stumped on how to access consts (like valid file formats) for error reporting given python relative import and package consideration (sys.path but idk I kinda don't want to)

# 12-24-2024
Resolve import error with sys.path update, thus far working implementation of error reporting pending actual unit tests (ugh) and reconsidering double-map of abbreviated error codes and the extended map categorizing errors in a human-readable way, but feel it still is worth it. Still pending design firm decision on default config as a script or ini on the dev side that does config if user given changeables are not specified, seeing main difference as whether configparser or manually fixing values in the script (without giving an option for savvy users to mess with the parts of the config that are fundamental to behind-the-scenes processing and internal parts of the code) or supporting dev-mode default.ini and also using it in conjunction with MANDATORY user config set for each generation of the specific bundle. Latter is least for actual desire as a design for lack of convenience for the user. Also obvious choice to split between default.ini and default.py

Functional validation of input dir but missing audio validation and import.

In any case, I am taking a break for holidays and prioritizing my health and medical treatment during my ADA leave. Scripting will resume when I've re-established a baseline balance with my life overall.

# 12-27-2024
Decided to work on this when my energy and health permits.

Design considerations (based on still using old, wonky version and re-analyzing that code):
1. Track storage for program generation of bundle should actually feature memoizing the NAME of the original audio file along with the number it has been assigned, and possibly label the track imported with the original audio file name (character limit?) for ease of use
2. Given that pyaudacity seems to have notable problems (on Windows?) of using write/read named pipes despite mod-pipe-script and no identifiable (as of yet) issues caused by macros / code errors and sometimes fails with that error and sometimes works, it seems to work better to split the bundle into smaller packages (batch size) to reduce investment / cost of re-attempting upon that error
3. Auto-amplify can be specified and applied if user (or dev?) threshold is identified as well as loudness normalization
4. Specify a single track as the 'loudest' track with the predominant noise - better sound and actually gives user choice / control over which subliminal to prioritize + for my own purposes I write custom subliminals and sometimes include them in bundles, and these should be the loudest if the bundle features me as a author rather than just bundler

First priority is unit-testing error and file/dir validation

Decided to make the error handler a class and use a string factory for validation and construction of error messages (?) just because. Let's see how it goes!