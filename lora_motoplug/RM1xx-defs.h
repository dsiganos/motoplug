//*****************************************************************************
//              Copyright (C) 2015 Laird Technologies
//
// Project:     RM1xx
//
// Module:      RM1XX-defs.H
//
// Notes:	This file contains all of the defintions that are commong between
// 			the C source code and the SmartBASIC applications written for this
// 			device.
//
//*****************************************************************************/



// Note: Due to the nature of the SmartBASIC applicaitions which will be including
// this file, the format must adhere to the following.
//
//			Allowed …
//			#define   SOMETHING     SOMEVALUE
//
//			Not Allowed …
//			#define   SOMEMACRO(_x_)     _x_
//			#if defined()
//			#ifdef
//			#else
//			#endif

// Options for get/set APIs                                            
#define LORAMAC_OPT_START                    1 // Beginning of the option enumeration 
#define LORAMAC_OPT_TX_POWER                 1 //RW - The output power in dB of the LoRa radio
#define LORAMAC_OPT_DATA_RATE                2 //RW - The data rate of the LoRa radio
#define LORAMAC_OPT_JOIN_STATE               3 //RO - The current Join state of the LoRa radio
#define LORAMAC_OPT_DEV_EUI                  4 //RO - The device EUI assigned by Laird 
#define LORAMAC_OPT_CUSTOM_DEV_EUI           5 //RW - An optional custom device EUI *not* provided by Laird
#define LORAMAC_OPT_DEV_ADDR                 6 //RW - The device address 
#define LORAMAC_OPT_APP_EUI                  7 //RW - The application EUI 
#define LORAMAC_OPT_APP_KEY                  8 //WO - The application key 
#define LORAMAC_OPT_VERSION                  9 //RO - The version number of the device
#define LORAMAC_OPT_RSSI                    10 //RO - The Received Signal Strength Indicator of the last recevied packet
#define LORAMAC_OPT_SNR                     11 //RO - The Signal-to-Noise Ratio of the last received packet
#define LORAMAC_OPT_DOWNLINK_COUNTER        12 //RO - The downlink packet count
#define LORAMAC_OPT_UPLINK_COUNTER          13 //RO - The uplink packet count
#define LORAMAC_OPT_SOURCE_VOLTAGE          14 //RO - The supply voltage in mV
#define LORAMAC_OPT_BIRTHDAY                16 //RO - Date of manufacturing for this device
#define LORAMAC_OPT_ADR_ENABLE              17 //RW - Enable/Disable Adaptive Data Rate (ADR) 
#define LORAMAC_OPT_CHANNELLIST             18 //RO - Lists all the enabled channels
#define LORAMAC_OPT_CHANNELMASK             19 //RO - Outputs the Channel mask
#define LORAMAC_OPT_NEXT_TX                 20 //RO - Time to next tx
#define LORAMAC_OPT_TEMPERATURE             21 //RO - Temperature in degrees Celsius
#define LORAMAC_OPT_TEMP_COMP_FACTOR        22 //RO - Temperature compensation factor - device specific
#define LORAMAC_OPT_FREQ_ERROR              23 //RO - Frequency error (in Hertz) of the SX1272
#define LORAMAC_OPT_FREQ_OFFSET             24 //RO - SX1272 Frequency offset calibrated for temperature
#define LORAMAC_OPT_MAX_RETRIES             25 //RW - Sets the maximum amount of times a packet can be transmitted without recevieing and acknowledgement
#define LORAMAC_OPT_END                     LORAMAC_OPT_MAX_RETRIES  // End of the option enumeration

// Private options not publicly documented
#define LORAMAC_PRIVATE_OPT_START           100
#define LORAMAC_OPT_DUTY_CYCLE_ENABLE       100 //RW - Enable/Disable the duty cycle checks
#define LORAMAC_OPT_RX2_DEFAULT_DATARATE    101 //RW - Sets the RX2 window defautl datarate.  This is only to get around a bug in the Semtech website.
#define LORAMAC_PRIVATE_OPT_END             LORAMAC_OPT_RX2_DEFAULT_DATARATE

// Special operating modes for development
#define LORAMAC_OPT_TEST_MODE               200 //RW - Enables/disables Test mode
#define LORAMAC_OPT_DEBUG_MODE              201 //RW - Enables/disables Debug mode


// Flags passed to LORAMACJoin
#define LORAMAC_JOIN_BY_REQUEST                  1 // Used with LORAMACJoin
#define LORAMAC_JOIN_BY_PERSONALIZATION          0 // Used with LORAMACJoin

// Flags passed to LORAMACTxData
#define LORAMAC_FLAG_TX_CONFIRMED                1 // Used with LORAMACTxData
#define LORAMAC_FLAG_TX_UNCONFIRMED              0 // Used with LORAMACTxData
