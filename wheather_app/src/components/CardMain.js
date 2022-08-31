import React from "react";
import axios from "axios";
import CitySelectMenu from "./CitySelectMenu";
import CardDaily from "./CardDaily";
import CardHourly from "./CardHourly";
import { weatherIcons } from "../constants";

class CardMain extends React.Component {
	constructor(props) {
		super(props);

		this.currentCity = {
			"name": "Moscow",
			"country": "Russia",
			"countryCode": "RU",
			};

		this.state = {
			menuActive: false, // флаг отображения меню выбора города
			cwResponse: null, // результат current weather запроса
			dwResponse: null, // результат daily weather запроса
			hwResponse: null, // результат hourly weather запроса
		};
	}

	setCurrentCity = (city) => {
		this.currentCity = city;
	};

	setMenuActive = (isActive) => {
		this.setState({ menuActive: isActive });
	};

	currentWeather() {
		const options = {
			method: "GET",
			url: "https://weatherbit-v1-mashape.p.rapidapi.com/current",
			params: { city: this.currentCity.name, country: this.currentCity.countryCode },
			headers: {
				"X-RapidAPI-Key": "fcb32d0d47msh7f5167c60ad5b2cp1a44f9jsnc23be5d0f196",
				"X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com",
			},
		};

		return axios.request(options);
	}

	// currentWeather() {
	// 	const options = {
	// 		method: "GET",
	// 		url: `http://localhost:3000/${this.currentCity.name}`,
	// 	};

	// 	return axios.request(options);
	// }

	dailyWeather() {
		const options = {
			method: "GET",
			url: `https://api.weatherbit.io/v2.0/forecast/daily?city=${this.currentCity.name}&country=${this.currentCity.countryCode}&days=5&key=284cb3b2eb644da581f99af668c89603`,
		};

		return axios.request(options);
	}

	hourlyWeather() {
		const options = {
			method: "GET",
			url: "https://weatherbit-v1-mashape.p.rapidapi.com/forecast/hourly",
			params: { city: this.currentCity.name, country: this.currentCity.countryCode, hours: 24 },
			headers: {
				"X-RapidAPI-Key": "fcb32d0d47msh7f5167c60ad5b2cp1a44f9jsnc23be5d0f196",
				"X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com",
			},
		};

		return axios.request(options);
	}

	async componentDidMount() {
		const cwResponse = await this.currentWeather();
		const dwResponse = await this.dailyWeather();
		const hwResponse = await this.hourlyWeather();
		this.setState({
			cwResponse: cwResponse.data.data[0],
			dwResponse: dwResponse.data.data,
			hwResponse: hwResponse.data.data
		});
		console.log(dwResponse);
		console.log(hwResponse);
	}

	render() {
		return (
			<>
				<div className="card card-1">
					<div id="demo" className="carousel slide" data-ride="carousel">
						{/* The slideshow */}
						<div className="carousel-inner">
							<div className="carousel-item active">
									<div className="row">
										<div className="col-6">
											<div className="temp">{this.state.cwResponse ? this.state.cwResponse.temp : null}&deg;</div>
											<div className="location" onClick={() => { this.setState({ menuActive: true }); }}>
												{this.currentCity.name}, {this.currentCity.country}</div>
											</div>
										<div className="col-6 justify-content-right">
											<img className="img-fluid" src={this.state.cwResponse ? weatherIcons[this.state.cwResponse.weather.description] : null} />
										</div>
									</div>
							</div>
						</div>
					</div>
				</div>
				<CitySelectMenu menuActive={this.state.menuActive} setMenuActive={this.setMenuActive}
					currentCity={this.currentCity} setCurrentCity={this.setCurrentCity}
					newResponse={() => this.componentDidMount()} />
				<CardDaily response={this.state.dwResponse} />
				<CardHourly response={this.state.hwResponse} />
			</>
		);
	}
}

export default CardMain;
