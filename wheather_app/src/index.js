import React from "react";
import ReactDOM from "react-dom";
import App from "./components/App";

const mountNode = ReactDOM.createRoot(document.getElementById("root"));
mountNode.render(
	<React.StrictMode>
		<App />
	</React.StrictMode>,
);
