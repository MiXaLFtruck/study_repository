import React from "react";
import { weatherIcons } from "../constants";

function CardHourly(props) {
	return (
	<div className="card card-2">
		<div id="demo" className="carousel slide" data-ride="carousel">

			{/* Indicators */}
			<ul className="carousel-indicators">
				<li data-target="#demo" data-slide-to="0"></li>
				<li data-target="#demo" data-slide-to="1" className="active"></li>
				<li data-target="#demo" data-slide-to="2"></li>
			</ul>

			{/* The slideshow */}
			<div className="carousel-inner">
				<div className="carousel-item active">
					<div className="row">
						<div className="col">
							<div className="row row1">{props.response ? props.response[0].temp : null}&deg;</div>
							<div className="row row2"><img className="img-fluid" src={props.response ? weatherIcons[props.response[0].weather.description] : null}/></div>
							<div className="row row3">{props.response ? props.response[0].timestamp_local.slice(11, 16) : null}</div>
							<div className="row row4">PM</div>
						</div>
						<div className="col">
							<div className="row row1">{props.response ? props.response[1].temp : null}&deg;</div>
							<div className="row row2"><img className="img-fluid" src={props.response ? weatherIcons[props.response[1].weather.description] : null}/></div>
							<div className="row row3">{props.response ? props.response[1].timestamp_local.slice(11, 16) : null}</div>
							<div className="row row4">PM</div>
						</div>
						<div className="col">
							<div className="row row1">{props.response ? props.response[2].temp : null}&deg;</div>
							<div className="row row2"><img className="img-fluid" src={props.response ? weatherIcons[props.response[2].weather.description] : null}/></div>
							<div className="row row3">{props.response ? props.response[2].timestamp_local.slice(11, 16) : null}</div>
							<div className="row row4">PM</div>
						</div>
						<div className="col">
							<div className="row row1">{props.response ? props.response[3].temp : null}&deg;</div>
							<div className="row row2"><img className="img-fluid" src={props.response ? weatherIcons[props.response[3].weather.description] : null}/></div>
							<div className="row row3">{props.response ? props.response[3].timestamp_local.slice(11, 16) : null}</div>
							<div className="row row4">PM</div>
						</div>
						<div className="col">
							<div className="row row1">{props.response ? props.response[4].temp : null}&deg;</div>
							<div className="row row2"><img className="img-fluid" src={props.response ? weatherIcons[props.response[4].weather.description] : null}/></div>
							<div className="row row3">{props.response ? props.response[4].timestamp_local.slice(11, 16) : null}</div>
							<div className="row row4">PM</div>
						</div>
					</div>

				</div>
			</div>

		</div>
	</div>
	);
}

export default CardHourly;
