## Getting started ambient-app--react front-end

### Install dependencies

Make sure you have Node.js (>= 18) and npm or yarn installed.

```
npm install
```


### Development

Start the development server:
```
npm start
```

The app should now be running at http://localhost:3000


Run tests:

```
npm test
```

### Project structure

Structure:
* `components/` - reusable React components 
* `containers/` - screens and other components that are not intended for reuse
* `utils/` - helpers
* `consts/` - constants
* `assets/` - images and other assets imported in React code

Code formatting:
* Use uppercase names for React Components files and related CSS files
* Use BEM naming convention for CSS classes - https://www.geeksforgeeks.org/css/understanding-the-css-bem-convention/
* Use ESLint (ToDo: add ESLint to project)
* Use "classnames" library to combine classnames

