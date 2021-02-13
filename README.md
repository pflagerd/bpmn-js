# bpmn-js - BPMN 2.0 for the web

[![Build Status](https://travis-ci.com/bpmn-io/bpmn-js.svg?branch=develop)](https://travis-ci.com/bpmn-io/bpmn-js)

View and edit BPMN 2.0 diagrams in the browser.

[![bpmn-js screencast](./resources/screencast.gif "bpmn-js in action")](http://demo.bpmn.io/s/start)


## Installation

Use the library [pre-packaged](https://github.com/bpmn-io/bpmn-js-examples/tree/master/pre-packaged)
or include it [via npm](https://github.com/bpmn-io/bpmn-js-examples/tree/master/bundling)
into your node-style web-application.

## Usage

To get started copy the code below to a local file (e.g. hello-viewer.html):

```javascript
<html>
<head>
  <title>hello-viewer</title>
  <script src="https://unpkg.com/bpmn-js@8.2.0/dist/bpmn-viewer.development.js"></script>
</head>
<body>
  <script>
    let c = document.createElement('div');
    document.body.appendChild(c);

    let viewer = new BpmnJS({ container: c });

    fetch('https://cdn.staticaly.com/gh/bpmn-io/bpmn-js-examples/dfceecba/starter/diagram.bpmn')
            .then(response => response.text())
            .then(xml => viewer.importXML(xml));
    </script>
</html>
```

Now load the file using a browser (Chrome, Firefox, etc.) and you will see a BPMN diagram:

![1611957113924](.md/README/1611957113924.png)




### Dynamic Attach/Detach

You may attach or detach the viewer dynamically to any element on the page, too:

```javascript
const viewer = new BpmnJS();

// attach it to some element
viewer.attachTo('#container');

// detach the panel
viewer.detach();
```


## Resources

* [Demo](http://demo.bpmn.io)
* [Issues](https://github.com/bpmn-io/bpmn-js/issues)
* [Examples](https://github.com/bpmn-io/bpmn-js-examples)
  * Checkout our [examples](https://github.com/bpmn-io/bpmn-js-examples) for many
    more supported usage scenarios.
* [Forum](https://forum.bpmn.io)
* [Changelog](./CHANGELOG.md)


## Build and Run

Prepare the project by installing all dependencies:

```sh
npm install
```

Then, depending on your use-case you may run any of the following commands:

```sh
# build the library and run all tests
npm run all

# spin up a single local modeler instance
npm start

# run the full development setup
npm run dev
```

You may need to perform [additional project setup](./docs/project/SETUP.md) when
building the latest development snapshot.

Please checkout our [contributing guidelines](./.github/CONTRIBUTING.md) if you plan to
file an issue or pull request.


## Related

bpmn-js builds on top of a few powerful tools:

* [bpmn-moddle](https://github.com/bpmn-io/bpmn-moddle): Read / write support for BPMN 2.0 XML in the browsers
* [diagram-js](https://github.com/bpmn-io/diagram-js): Diagram rendering and editing toolkit


## License

Use under the terms of the [bpmn.io license](http://bpmn.io/license).
