import React from 'react';
import { StyleSheet, Text, View, TouchableOpacity, Image } from 'react-native';

export class CategoryCard extends React.Component {

    constructor(props){
        super(props);
        this.state = {
            text: this.props.category,
        };
    }

    render() {
        return (
            <View style={styles.card}>
                <View style={styles.categoryContainer}>
                    <Text style={styles.cardText}>{this.state.text}</Text> 
                </View>
            </View>
        )
    }
}

const styles = StyleSheet.create({
    card: {
        flex: 1,
        backgroundColor: "#19297C",
        marginHorizontal: 8,
        marginVertical: 8,
        height: 225,
        marginBottom: 20,
        borderRadius: 10,
    },

    cardText: {
        fontSize: 15,
        fontFamily: 'AvenirNext-Bold',
        color: 'black',
    },

    categoryContainer: {
        backgroundColor: 'white',
        top: 25,
        left: -10,
        width: '95%',
        height: '17%',
        borderRadius: 10,
        paddingLeft: 10,
        justifyContent: 'center',
        alignItems: 'center',
    },
})