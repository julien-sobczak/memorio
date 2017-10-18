# \<Memorio\>

Games using popular memory techniques

## Install the Polymer-CLI

First, make sure you have the [Polymer CLI](https://www.npmjs.com/package/polymer-cli) installed. Then run `polymer serve` to serve your application locally.

## Install the Firebase Tools

Second, make sure you have the [Firebase Tools](https://github.com/firebase/firebase-tools) including a CLI to connect to your Firebase application.

```
$ npm install -g firebase-tools
```

Then, login:

```
$ firebase login
```

If it is your first time with Firebase, you need to initialize the project (make sure to check all features):

```
$ firebase init
```

Otherwise, you have nothing to do.

```
$ firebase use
```

Great! You are ready to deploy your application, use the database, or create Cloud functions.

## Viewing Your Application

```
$ polymer serve
```

## Building Your Application

```
$ polymer build
```

This will create builds of your application in the `build/` directory, optimized to be served in production. You can then serve the built versions by giving `polymer serve` a folder to serve from:

```
$ polymer serve build/default
```

## Running Tests

```
$ polymer test
```

Your application is already set up to be tested via [web-component-tester](https://github.com/Polymer/web-component-tester). Run `polymer test` to run your application's test suite locally.


## Building

Run the command:

```
$ polymer build
```


## Deploying (with Firebase Hosting)

Check the [official documentation](https://www.polymer-project.org/2.0/start/toolbox/deploy#deploy-with-firebase)

To deploy, run the command:

```
$ firebase deploy
```

The URL is printed but you can also access the application using the command:

```
$ firebase open hosting:site
```
