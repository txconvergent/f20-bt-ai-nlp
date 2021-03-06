import React from 'react';
import { StyleSheet, Text, View, TouchableOpacity, Image } from 'react-native';

const images = {
    twitter: require('../assets/twitter_blue.png'),
    horns_link: require('../assets/ut_logo.png'),
    news: require('../assets/news_icon.png'),
}

export class Card extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            text: props.text,
            source: props.source,
            sourceText: props.sourceText,
            category: props.category,
        };
    }

    render() {

        var image = images.twitter;
        if(this.state.source == "Twitter") {
            image = images.twitter;
        }
        else if(this.state.source == "HornsLink") {
            image = images.horns_link;
        }
        else if(this.state.source == "News") {
            image = images.news;
        }


        return (
            <View style={styles.card}>
                <View style={styles.sourceContainer}>
                    <Image style={styles.sourceImage} source={image}/>
                    <Text style={styles.sourceText}>{this.state.sourceText}</Text>
                </View>

                <View style={styles.categoryContainer}>
                    <Text style={styles.categoryText}>{this.state.category}</Text>
                </View>

                <View style={styles.bodyContainer}>
                    <Text style={styles.cardBodyText}>{this.state.text}</Text>
                </View>
        
                <TouchableOpacity style={styles.cardInfoButton} activeOpacity={0.6}>
                    <Text style={styles.cardInfoButtonText}>info and source</Text>
                </TouchableOpacity>
            </View>
        )
    }
}

const styles = StyleSheet.create({
    card: {
        flex: 1,
        borderRadius: 25,
        borderWidth: 2,
        borderColor: '#22AED1',
        justifyContent: "center",
        backgroundColor: "#19297C",
        alignItems: 'center',
    },

    cardBodyText: {
        textAlign: 'left',
        fontSize: 25,
        backgroundColor: "transparent",
        color: 'white',
        fontFamily: 'Avenir',
    },

    bodyContainer: {
        position: 'absolute',
        width: '85%',
    },

    cardInfoButton: {
        position: 'absolute',
        flexDirection: 'row',
        backgroundColor: 'white',
        justifyContent: 'center',
        alignItems: 'center',
        borderRadius: 15,
        bottom: 30,
        width: '90%',
        height: '10%',
    },

    cardInfoButtonText: {
        fontSize: 25,
        fontFamily: 'Avenir',
    },

    sourceContainer: {
        position: 'absolute',
        height: '19%',
        top: 10,
        left: 10,
    },

    sourceImage: {
        width: 60,
        height: 60,
        left: 10,
        top: 5,
        backgroundColor: 'transparent',
    },

    sourceText: {
        fontSize: 20,
        marginLeft: 10,
        marginTop: 10,
        color: 'white',
        fontFamily: 'AvenirNext-Bold',
    },

    categoryContainer: {
        position: 'absolute',
        top: '5%',
        height: '8%',
        right: -10,
        width: '50%',
        borderRadius: 10,
        justifyContent: 'center',
        backgroundColor: 'white',
        paddingLeft: 15,
    },

    categoryText: {
        fontSize: 15,
        fontFamily: 'AvenirNext-Bold',
        color: 'black',
    }
});
