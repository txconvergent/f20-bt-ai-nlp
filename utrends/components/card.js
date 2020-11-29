import React from 'react';
import { StyleSheet, Text, View, TouchableOpacity, Image } from 'react-native';

export class Card extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            text: props.text,
            category: props.category,
        };
    }

    render() {
        console.log(this.state.text);
        return (
            <View style={styles.card}>
                <View style={styles.sourceContainer}>
                    <Image style={styles.sourceImage} source={require('../assets/twitter_blue.png')}/>
                    <Text style={styles.sourceText}>@DailyTexan</Text>
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
        borderColor: "white",
        justifyContent: "center",
        backgroundColor: "#19297C",
        alignItems: 'center',
    },

    cardBodyText: {
        textAlign: 'left',
        fontSize: 30,
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
        width: 75,
        height: 75,
        backgroundColor: 'transparent',
    },

    sourceText: {
        fontSize: 20,
        marginLeft: 10,
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
