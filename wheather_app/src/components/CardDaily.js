import React from "react";
import { weatherIcons, weekDays } from "../constants";

class CardDaily extends React.Component {
	static getWeekDay(stringDate) {
		const date = new Date(stringDate);
		return date.getDay();
	}

	render() {
		return (
			<div className="card card-3">
			<div id="demo" className="carousel slide" data-ride="carousel">

				{/* Indicators */}
				<ul className="carousel-indicators">
					<li data-target="#demo" data-slide-to="0"></li>
					<li data-target="#demo" data-slide-to="1"></li>
					<li data-target="#demo" data-slide-to="2" className="active"></li>
				</ul>

				{/* The slideshow */}
				<div className="carousel-inner">
					<div className="carousel-item active">
						<div className="row">
							<div className="col">
								<div className="row row1">{this.props.response ? this.props.response[0].temp : null}&deg;</div>
								<div className="row row2"><img className="img-fluid" src={this.props.response ? weatherIcons[this.props.response[0].weather.description] : null}/></div>
								<div className="row row3">{this.props.response ? weekDays[CardDaily.getWeekDay(this.props.response[0].datetime)] : null}</div>
							</div>
							<div className="col">
								<div className="row row1">{this.props.response ? this.props.response[1].temp : null}&deg;</div>
								<div className="row row2"><img className="img-fluid" src={this.props.response ? weatherIcons[this.props.response[1].weather.description] : null}/></div>
								<div className="row row3">{this.props.response ? weekDays[CardDaily.getWeekDay(this.props.response[1].datetime)] : null}</div>
							</div>
							<div className="col">
								<div className="row row1">{this.props.response ? this.props.response[2].temp : null}&deg;</div>
								<div className="row row2"><img className="img-fluid" src={this.props.response ? weatherIcons[this.props.response[2].weather.description] : null}/></div>
								<div className="row row3">{this.props.response ? weekDays[CardDaily.getWeekDay(this.props.response[2].datetime)] : null}</div>
							</div>
							<div className="col">
								<div className="row row1">{this.props.response ? this.props.response[3].temp : null}&deg;</div>
								<div className="row row2"><img className="img-fluid" src={this.props.response ? weatherIcons[this.props.response[3].weather.description] : null}/></div>
								<div className="row row3">{this.props.response ? weekDays[CardDaily.getWeekDay(this.props.response[3].datetime)] : null}</div>
							</div>
							<div className="col">
								<div className="row row1">{this.props.response ? this.props.response[4].temp : null}&deg;</div>
								<div className="row row2"><img className="img-fluid" src={this.props.response ? weatherIcons[this.props.response[4].weather.description] : null}/></div>
								<div className="row row3">{this.props.response ? weekDays[CardDaily.getWeekDay(this.props.response[4].datetime)] : null}</div>
							</div>
						</div>

					</div>
				</div>

			</div>
		</div>
		);
	}
}
export default CardDaily;
